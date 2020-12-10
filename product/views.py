# -*- coding: utf-8 -*-
from pip._internal import req
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import ProductModel
from rest_framework import status
from django.core import serializers


@api_view(['GET'])
def get_all_product(request):
    if request.method == 'GET':
        products = ProductModel.get_all_product()
        return Response(products,status=status.HTTP_200_OK)
@api_view(['POST'])
def insert_product(request):
    return Response("123",status.HTTP_200_OK)
@api_view(['GET','POST','PUT','DELETE'])
def product_api_view(request,product_id):
    if request.method == 'POST':
        product = ProductModel.get_by_product_id(product_id)
        return Response(product,status=status.HTTP_200_OK)
