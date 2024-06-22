from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import address, company, phone_number

from api.suppliers.models import Supplier

fake = Faker()

fake.add_provider(company)
fake.add_provider(address)
fake.add_provider(phone_number)


class Command(BaseCommand):
    help = "Create suppliers"

    def add_arguments(self, parser):
        parser.add_argument(
            "num_suppliers", type=int, help="The number of suppliers to create"
        )

    def handle(self, *args, **kwargs):
        num_suppliers = kwargs["num_suppliers"]

        suppliers = []
        for _ in range(num_suppliers):
            supplier_name = fake.company()
            supplier_contact_info = f"{fake.phone_number()}, {fake.address()}"

            supplier = Supplier(
                name=supplier_name,
                contact_info=supplier_contact_info,
            )
            suppliers.append(supplier)

        Supplier.objects.bulk_create(suppliers)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {num_suppliers} suppliers.")
        )
