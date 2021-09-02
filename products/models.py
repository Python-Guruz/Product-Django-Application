from django.db import models
import uuid

# Create your models here.

class products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, blank=False, null=False)
    price = models.IntegerField(default=0)
    quantity = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name
