from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import OrderModelSerializer, OrderCreateModelSerializer


class OrderViewSet(viewsets.ViewSet):

    def dispatch(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        return super().dispatch(request, *args, **kwargs)

    def create(self, request):

        serializer = OrderCreateModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'message': 'Order created',
            'status': True,
            'data': OrderModelSerializer(serializer.instance).data,
        }

        return Response(data, status=status.HTTP_201_CREATED)
