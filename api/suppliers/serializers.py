from rest_framework import serializers

from api.inventory.models import Item

from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, required=False
    )

    class Meta:
        model = Supplier
        fields = ["id", "name", "contact_info", "items"]
        read_only_fields = ["items"]


class SupplierItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "price",
            "date_added",
            "suppliers",
        ]
        read_only_fields = ["date_added", "suppliers"]
