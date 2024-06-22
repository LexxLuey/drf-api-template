from django.db import models

from core.models.model import BaseModel


class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name
