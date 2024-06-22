from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Supplier
from .serializers import SupplierItemSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=["get"])
    def items(self, request, pk=None):
        """
        List Items of supplier instance
        """
        supplier = self.get_object()
        items = supplier.items.all()
        serializer = SupplierItemSerializer(items, many=True, read_only=True)
        return Response(serializer.data)
