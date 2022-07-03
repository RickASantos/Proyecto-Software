from pyexpat import model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    UNIT_CHOICES = [
        (1, 'kg'),
        (2, 'g'),
        (3, 'l'),
        (4, 'ml'),
        (5, 'und'),
        (6, 'paq'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    product_unit = models.IntegerField(choices=UNIT_CHOICES)
    quantity = models.PositiveIntegerField()

    # definimos 3 tipos de status :
    # 1 => en inventario
    # 2 => out stock
    # 3 => pedido

    STATUS_CHOICES = [
        (1, 'en inventario'),
        (2, 'out stock'),
        (3, 'pedido'),
    ]

    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
