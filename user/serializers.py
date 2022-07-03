from rest_framework import serializers

from .models import User, Profile, TypeUser, Role


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'address',
            'city',
            'phone',
            'avatar',
        )


class ProfileUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fiedls = ('address', 'city', 'phone', 'avatar')


class TypeUserModelSerializer(serializers.ModelSerializer):
    type_user = serializers.SerializerMethodField()

    class Meta:
        model = TypeUser
        fields = (
            'type_user',
        )

    def get_type_user(self, data):
        POSITION_TYPE_OPTIONS = {
            '1': 'employee',
            '2': 'admin'
        }
        return POSITION_TYPE_OPTIONS[str(data.type_user)]


class UserSerializer(serializers.ModelSerializer):

    typeuser = TypeUserModelSerializer()
    profile = ProfileModelSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'typeuser',
            'profile'
        )
        read_only_fields = ('id', 'email')


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
        serializers para la actualizacion del user profile 
    """

    profile = ProfileModelSerializer(required=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop(
            'profile') if 'profile' in validated_data else {}
        profile = instance.profile

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        for key, value in profile_data.items():
            setattr(profile, key, value)
        profile.save()

        return instance


class UserSerializerUpdateProfileImage(serializers.ModelSerializer):
    """
        serializers para la actualizacion del user profile 
    """

    class Meta:
        model = Profile
        fields = ('avatar',)

    def update(self, instance, validated_data):
        
        ## save image in server
        with open('media/avatar/' + validated_data['avatar'].name, 'wb+') as destination:
            for chunk in validated_data['avatar'].chunks():
                destination.write(chunk)
        path_file = '/avatar/' + validated_data['avatar'].name
        
        instance.profile.avatar = path_file
        return instance
