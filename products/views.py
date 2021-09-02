from django.shortcuts import render
from products.serializers import ProductSerializer
from products.models import products
from rest_framework.response import response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])

def products(request):
    if request.method == 'GET':
        product = products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({'data':data.serializer},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid:

            serializer.save()
            return Response({"message":"The dog has been created successfully",
                            "data" : serializer.data

            },status.HTTP_201_CREATED)
        
