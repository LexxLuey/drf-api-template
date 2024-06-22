from rest_framework.test import APIClient, APITestCase

from api.inventory.models import Item
from api.suppliers.models import Supplier


class TestListItems(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )
        data = {
            "name": "string",
            "description": "string",
            "price": "917.09",
            "date_added": "2024-06-21",
        }

        items = []
        for num in range(100):
            item_data = data.copy()
            item_data["name"] = f'{data["name"]}{num}'
            item = Item(**item_data)
            items.append(item)

        created_items = Item.objects.bulk_create(items)

        for item in created_items:
            item.suppliers.add(supplier)

    def test_list_items_success(self):
        response = self.client.get("/api/inventory/", format="json")
        self.assertEqual(response.status_code, 200)
