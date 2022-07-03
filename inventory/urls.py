from django.urls import path

from .views import InventoryView,CategoryView

app_name = 'inventory'

urlpatterns = [
    path('', InventoryView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='product'),
    path('<int:pk>/', InventoryView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='inventory'),

    path('category/', CategoryView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='category'),

]
