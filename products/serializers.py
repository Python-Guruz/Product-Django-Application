from django.db.models import fields
from rest_framework import serializers
from products.models import products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model : products
        fields : ('id','name','price','quantity')

        def save(self,*args,**kwargs):
            Product = products(
                name = self.validated_data['name'],
                price = self.validated_data['price'],
                quantity = self.validated_data['quantity']

            )
            Product.save()
            return Product
