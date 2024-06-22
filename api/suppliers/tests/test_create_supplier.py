from rest_framework.test import APIClient, APITestCase

from api.suppliers.models import Supplier


class TestCreateSupplier(APITestCase):

    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    def test_create_supplier_success(self):
        data = {
            "name": "string",
            "contact_info": "string",
        }

        response = self.client.post("/api/suppliers/", data=data, format="json")
        res = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(res["name"], data["name"])

    def test_create_supplier_failure_missing_data(self):
        data = {"name": "Test Supplier"}  # Missing title
        response = self.client.post("/api/suppliers/", data=data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Supplier.objects.count(), 0)
