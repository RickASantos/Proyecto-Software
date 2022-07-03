from itertools import product
from rest_framework import serializers

from .models import Product, Category


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = ('name',)


class ProductModelSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    product_unit = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'product_unit',
                  'quantity', 'status', 'category', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def get_product_unit(self, obj):
        UNIT_CHOICES = [
            (1, 'kg'),
            (2, 'g'),
            (3, 'l'),
            (4, 'ml'),
            (5, 'und'),
            (6, 'paq'),
        ]
        return dict(UNIT_CHOICES).get(obj.product_unit)
