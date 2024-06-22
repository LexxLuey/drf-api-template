from rest_framework import serializers

from .models import Item, Supplier


class ItemSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "contact_info"]


class ItemSerializer(serializers.ModelSerializer):
    suppliers = ItemSupplierSerializer(many=True, read_only=False, required=False)
    suppliers_id = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "price",
            "date_added",
            "suppliers",
            "suppliers_id",
        ]
        read_only_fields = ["created_at", "modified_at"]

    def create(self, validated_data):
        suppliers_id = validated_data.pop("suppliers_id", [])
        suppliers_data = validated_data.pop("suppliers", [])

        item = Item.objects.create(**validated_data)

        if suppliers_id:
            suppliers = Supplier.objects.filter(id__in=suppliers_id)
            item.suppliers.add(*suppliers)

        if suppliers_data:
            supplier_objs = [Supplier(**data) for data in suppliers_data]
            created_suppliers = Supplier.objects.bulk_create(supplier_objs)
            item.suppliers.add(*created_suppliers)

        return item

    def update(self, instance, validated_data):
        suppliers_id = validated_data.pop("suppliers_id", [])
        suppliers_data = validated_data.pop("suppliers", [])

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.save()

        if suppliers_id:
            suppliers = Supplier.objects.filter(id__in=suppliers_id)
            instance.suppliers.set(suppliers)

        if suppliers_data:
            supplier_objs = [Supplier(**data) for data in suppliers_data]
            created_suppliers = Supplier.objects.bulk_create(supplier_objs)
            instance.suppliers.add(*created_suppliers)

        return instance
