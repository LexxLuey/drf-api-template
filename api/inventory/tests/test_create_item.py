from rest_framework.test import APIClient, APITestCase

from api.inventory.models import Item
from api.suppliers.models import Supplier


class TestCreateItem(APITestCase):

    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    def test_create_item_success(self):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )
        data = {
            "name": "string",
            "description": "string",
            "price": "917.09",
            "date_added": "2024-06-21",
            "suppliers": [{"name": "stringo", "contact_info": "stringo"}],
            "suppliers_id": [supplier.pk],
        }

        response = self.client.post("/api/inventory/", data=data, format="json")
        res = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(res["name"], data["name"])

    def test_create_item_failure_missing_data(self):
        data = {"name": "Test Item"}  # Missing title
        response = self.client.post("/api/inventory/", data=data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Item.objects.count(), 0)
