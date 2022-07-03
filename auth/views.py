
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


from .serializers import LoginUserSerializer, UserCreateSerializer
from user.serializers import UserSerializer


class AdminUserViewset(ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = UserCreateSerializer(
            data=request.data, context={'position': 'admin'})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Admin created',
            'status': True,
            'data': UserSerializer(serializer.instance).data
        }

        return Response(data, status=status.HTTP_201_CREATED)


class EmployeeUserRegisterView(ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = UserCreateSerializer(
            data=request.data, context={'position': 'employee'})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Employee created',
            'status': True,
            'data': UserSerializer(serializer.instance).data
        }

        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, tokens = serializer.save()

        data = {
            'message': 'Login successful',
            'status': True,
            'user': UserSerializer(user).data,
            'token': tokens
        }
        
        return Response(data, status=status.HTTP_200_OK)
