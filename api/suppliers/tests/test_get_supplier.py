from rest_framework.test import APIClient, APITestCase

from api.suppliers.models import Supplier


class TestGetSupplier(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )

        cls.supplier_id = supplier.pk
        cls.supplier = supplier

    def test_get_supplier_success(self):
        response = self.client.get(f"/api/suppliers/{self.supplier_id}/", format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], self.supplier.name)

    def test_get_supplier_not_found(self):
        invalid_id = 100  # Non-existent supplier ID
        response = self.client.get(f"/api/suppliers/{invalid_id}/", format="json")
        self.assertEqual(response.status_code, 404)
