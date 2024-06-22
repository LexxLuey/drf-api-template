import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from faker.providers import internet, lorem, person

from api.inventory.models import Item
from api.suppliers.models import Supplier

fake = Faker()

fake.add_provider(internet)
fake.add_provider(person)
fake.add_provider(lorem)


class Command(BaseCommand):
    help = "Create items and randomly attach them to one or more suppliers"

    def add_arguments(self, parser):
        parser.add_argument("num_items", type=int, help="The number of items to create")

    def handle(self, *args, **kwargs):
        num_items = kwargs["num_items"]
        suppliers = list(Supplier.objects.all())

        if not suppliers:
            self.stdout.write(
                self.style.ERROR("No suppliers found. Please add some suppliers first.")
            )
            return

        items = []
        for i in range(num_items):
            item_name = fake.military_apo()
            item_description = fake.catch_phrase()
            item_price = random.uniform(10.0, 100.0)
            item_date_added = timezone.now()

            item = Item(
                name=item_name,
                description=item_description,
                price=item_price,
                date_added=item_date_added,
            )
            items.append(item)

        created_items = Item.objects.bulk_create(items)

        for item in created_items:
            num_suppliers = random.randint(1, len(suppliers))
            attached_suppliers = random.sample(suppliers, num_suppliers)
            item.suppliers.add(*attached_suppliers)

            self.stdout.write(
                self.style.SUCCESS(
                    f'Created item "{item.name}" and attached {num_suppliers} suppliers.'
                )
            )
