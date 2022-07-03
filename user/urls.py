from django.urls import path, re_path

from .views import UserViewSet, UpLoadImageAvatar

app_name = 'user'
urlpatterns = [
    path('employee/', UserViewSet.as_view({
        'get': 'list'
    }), name='list'),
    path('employee/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='list'),
    path('employee/upload-avatar/',UpLoadImageAvatar.as_view(), name='upload'),

]
