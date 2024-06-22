from django.db import models

from api.suppliers.models import Supplier
from core.models.model import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(null=True)
    suppliers = models.ManyToManyField(Supplier, related_name="items")

    def __str__(self):
        return self.name
