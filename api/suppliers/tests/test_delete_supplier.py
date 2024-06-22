from rest_framework.test import APIClient, APITestCase

from api.suppliers.models import Supplier


class TestDeleteSupplier(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )

        cls.supplier_id = supplier.pk

    def test_delete_supplier_success(self):
        response = self.client.delete(f"/api/suppliers/{self.supplier_id}/", format="json")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Supplier.objects.count(), 0)

    def test_delete_supplier_not_found(self):
        invalid_id = 100  # Non-existent supplier ID
        response = self.client.delete(f"/api/suppliers/{invalid_id}/", format="json")
        self.assertEqual(response.status_code, 404)
