from rest_framework.test import APIClient, APITestCase

from api.inventory.models import Item
from api.suppliers.models import Supplier


class TestDeleteItem(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

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

    def test_delete_item_success(self):
        response = self.client.delete(f"/api/inventory/{self.item_id}/", format="json")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Item.objects.count(), 0)

    def test_delete_item_not_found(self):
        invalid_id = 100  # Non-existent item ID
        response = self.client.delete(f"/api/inventory/{invalid_id}/", format="json")
        self.assertEqual(response.status_code, 404)
