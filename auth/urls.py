from django.urls import path

from .views import AdminUserViewset, LoginView, EmployeeUserRegisterView


app_name = 'auth'
urlpatterns = [
    path('admin/', AdminUserViewset.as_view({'post': 'create'})),
    path('employee/', EmployeeUserRegisterView.as_view({
        'post': 'create',
    })),
    path('login/', LoginView.as_view(), name='login'),
]
