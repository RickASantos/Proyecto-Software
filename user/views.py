
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminUser, IsEmployeeUser
from user.models import User
from .serializers import UserSerializer, UserProfileUpdateSerializer, UserSerializerUpdateProfileImage


class UserViewSet(viewsets.ViewSet):

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['retrieve', 'update', 'list', 'profile']:
            permissions = [IsAuthenticated, IsAdminUser]
        elif self.action in ['retrieve']:
            permissions = [IsAuthenticated, IsEmployeeUser]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def list(self, request):

        employess = User.objects.filter(typeuser__type_user=1, is_active=True)

        data = {
            'message': 'Employees list',
            'status': True,
            'employees': UserSerializer(employess, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        employee = get_object_or_404(User.objects.filter(
            typeuser__type_user=1, is_active=True), pk=pk)

        data = {
            'message': 'Employee retrieved',
            'status': True,
            'employee': UserSerializer(employee).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        employee = get_object_or_404(
            User.objects.filter(typeuser__type_user=1, is_active=True), pk=pk)
        serializer = UserProfileUpdateSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Employee updated',
            'status': True,
            'employee': UserSerializer(serializer.instance).data
        }

        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):

        employee = get_object_or_404(
            User.objects.filter(typeuser__type_user=1, is_active=True), pk=pk)

        employee.is_active = False
        employee.save()

        data = {
            'message': 'Employee deleted',
            'status': True,
        }
        return Response(data, status=status.HTTP_200_OK)


class UpLoadImageAvatar(APIView):

    def post(self, request):
        user = request.user
        file = request.data['file']
        filename = file.name

        data = {
            'avatar': file,
        }
        serializer = UserSerializerUpdateProfileImage(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # path = settings.MEDIA_ROOT + '/avatar/'

        # # create foder if not exists
        # if not os.path.exists(path):
        #     os.makedirs(path)

        # with open(path, 'wb+') as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)

        # user.profile.avatar = 'avatar/' + filename
        # user.save()

        data = {
            'message': 'Avatar updated',
            'status': True,
            'user': UserSerializer(user).data
        }
        return Response(data, status=status.HTTP_200_OK)
