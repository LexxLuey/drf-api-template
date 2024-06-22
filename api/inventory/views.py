from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer, ItemSupplierSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=["get"])
    def suppliers(self, request, pk=None):
        """
        List Suppliers of Inventory Item instance
        """
        item = self.get_object()
        suppliers = item.suppliers.all()
        serializer = ItemSupplierSerializer(suppliers, many=True, read_only=True)
        return Response(serializer.data)
