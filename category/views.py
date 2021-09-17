from django.shortcuts import render
from category.serializers import CategorySerializer
from category.models import products
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])

def category(request):
    if request.method == 'GET':
        Category = category.objects.all()
        serializer = CategorySerializer(Category, many=True)
        return Response({'data':serializer.data},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid:

            serializer.save()
            return Response({"message":"The product has been created successfully",
                            "data" : serializer.data
                            
            },status.HTTP_201_CREATED)
        

