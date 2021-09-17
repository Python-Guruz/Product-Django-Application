from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
        id = models.UUIDField(primary_key = True,default=uuid.uuid4,editable=False)
        type = models.CharField(max_length=300, blank=False, null= False)
        #manufacture_date =models.DateField(manufacture_date= 12-7-21, null=False,blank=False)
        #expiry_date = models.DateField(expiry_date= 30-7-25, null= False, blank = False)

        def __str__(self):
                return self.name
        
