from rest_framework.test import APIClient, APITestCase

from api.suppliers.models import Supplier


class TestUpdateSupplier(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Create a DRF test client instance

    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(
            name="string",
            contact_info="string",
        )

        cls.supplier_id = supplier.pk

    def test_update_supplier_success(self):
        data = {"name": "Updated Supplier Name"}
        response = self.client.patch(
            f"/api/suppliers/{self.supplier_id}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Supplier.objects.get(id=self.supplier_id).name, data["name"])

    def test_update_supplier_not_found(self):
        invalid_id = 100  # Non-existent supplier ID
        data = {"title": "Updated Supplier Title"}
        response = self.client.put(
            f"/api/suppliers/{invalid_id}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 404)
