from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TypeUser(models.Model):

    POSITION_TYPE_OPTIONS = [
        (1, 'employee'),
        (2, 'admin'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    type_user = models.IntegerField(choices=POSITION_TYPE_OPTIONS)
    roles = models.ForeignKey(
        Role, on_delete=models.CASCADE, blank=True, null=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.FileField(upload_to='avatar', blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
