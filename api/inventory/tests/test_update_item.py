from rest_framework.test import APIClient, APITestCase

from api.inventory.models import Item
from api.suppliers.models import Supplier


class TestUpdateItem(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance
        self.supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )

    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )
        item = Item.objects.create(
            name="string", description="string", price="917.09", date_added="2024-06-21"
        )

        item.suppliers.set([supplier])

        cls.item_id = item.pk

    def test_update_item_success(self):
        data = {"name": "Updated Item Name"}
        response = self.client.patch(
            f"/api/inventory/{self.item_id}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.get(id=self.item_id).name, data["name"])

    def test_update_item_not_found(self):
        invalid_id = 100  # Non-existent item ID
        data = {"title": "Updated Item Title"}
        response = self.client.put(
            f"/api/inventory/{invalid_id}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 404)
