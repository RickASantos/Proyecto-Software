from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductModelSerializer, CategoryModelSerializer


class CategoryView(viewsets.ViewSet):

    def list(self, request):
        categories = Category.objects.all().order_by('-created_at')
        serializer = CategoryModelSerializer(categories, many=True)

        data = {
            'message': 'Listado de categorias',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CategoryModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Categoria creado',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_201_CREATED)


class InventoryView(viewsets.ViewSet):
    """
      Usaremos viewset ya que nos trae metodos default para listar, crear, detail, update, delete
    """

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)

        data = {
            'message': 'Listado de productos',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Producto creado',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):

        product = get_object_or_404(Product, pk=pk)
        serializer = ProductModelSerializer(product)

        data = {
            'message': 'Producto encontrado',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Producto actualizado',
            'status': True,
            'data': serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()

        data = {
            'message': 'Producto eliminado',
            'status': True,
        }

        return Response(data, status=status.HTTP_200_OK)
