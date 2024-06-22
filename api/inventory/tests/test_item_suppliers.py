from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.inventory.models import Item
from api.suppliers.models import Supplier


class TestItemSuppliers(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.supplier = Supplier.objects.create(
            name="Supplier1", contact_info="Contact1"
        )

        self.item = Item.objects.create(
            name="Item1",
            description="Description1",
            price=100.0,
            date_added="2024-06-21",
        )
        self.item.suppliers.add(self.supplier)

    def test_get_item_suppliers(self):
        response = self.client.get(f"/api/inventory/{self.item.pk}/suppliers/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], self.supplier.name)
