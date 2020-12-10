# -*- coding: utf-8 -*-
import json

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

@api_view(['POST'])
def search_product(request):
    try:
        body = json.loads(request.body)
        text_search = body['text_search']
        products = ProductModel.search(text_search=text_search)
        return Response(products, status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','POST','PUT','DELETE'])
def product_api_view(request,product_id):
    if request.method == 'POST':
        product = ProductModel.get_by_product_id(product_id)
        return Response(product,status=status.HTTP_200_OK)
