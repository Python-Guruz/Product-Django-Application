from django.db.models import fields
from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model : Category
        fields = ('id','type')

        def save(self,*args,**kwargs):
            category: Category(
            type = self.validated_data['type']
            )

            category.save()
            return category


