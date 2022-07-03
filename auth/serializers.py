from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation
from rest_framework_simplejwt.authentication import authentication
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
from user.models import User, TypeUser, Profile


class UserCreateSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    password = serializers.CharField(min_length=6, max_length=64)
    password2 = serializers.CharField(min_length=6, max_length=64)
    first_name = serializers.CharField(min_length=2, max_length=60)
    last_name = serializers.CharField(min_length=2, max_length=60)

    def validate(self, data):

        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError("Password don't match")

        password_validation.validate_password(password)
        return data

    def create(self, data):

        data.pop('password2')
        data = {
            **data,
            "username": data['email'],
        }

        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)
        # register type of user
        position = self.context['position']
        if position == 'admin':
            position = 2
        elif position == 'employee':
            position = 1

        TypeUser.objects.create(user=user, type_user=position)

        return user


class LoginUserSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""

        user = authentication.authenticate(
            username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('User is not active')

        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token = RefreshToken.for_user(self.context['user'])

        tokens = {
            'access': str(token.access_token),
            'refresh': str(token)
        }

        return self.context['user'], tokens
