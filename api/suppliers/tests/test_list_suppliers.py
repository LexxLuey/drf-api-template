from rest_framework.test import APIClient, APITestCase

from api.suppliers.models import Supplier


class TestListSuppliers(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    @classmethod
    def setUpTestData(cls):
        data = {
            "name": "string",
            "contact_info": "string",
        }

        suppliers = []
        for num in range(100):
            supplier_data = data.copy()
            supplier_data["name"] = f'{data["name"]}{num}'
            supplier = Supplier(**supplier_data)
            suppliers.append(supplier)

        Supplier.objects.bulk_create(suppliers)

    def test_list_suppliers_success(self):
        response = self.client.get("/api/suppliers/", format="json")
        self.assertEqual(response.status_code, 200)
