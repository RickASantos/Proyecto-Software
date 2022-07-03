from rest_framework import serializers

from .models import Order


class OrderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id',
            'client',
            'employee',
            'total',
            'tip',
        )

class OrderCreateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'client',
            'employee',
            'total',
        )
