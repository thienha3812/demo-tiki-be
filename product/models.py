# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import html
from django.core import serializers
from django.db import models

# Create your models here.
from bs4 import BeautifulSoup
from html import  HTML
import json
from review.models import Review
from sku.models import SKU


class ProductImage(models.Model):
    src = models.CharField(max_length=255)
    size = models.FloatField()
    type = models.CharField(max_length=255)
    created_time = models.TimeField(auto_now=True)
    product_id = models.IntegerField()
    @classmethod
    def find_by_id(cls,id):
        image = cls.objects.filter(id=id).values()
        if image[:1]:
            return image[0]
        else:
            return None

class ProductModel(models.Model):
    product_name = models.TextField(max_length=350)
    product_price = models.FloatField(default=0)
    sku_id = models.IntegerField(null=True,default=0)
    unit_in_stock = models.IntegerField(default=1)
    discount = models.IntegerField(default=0)
    category_id = models.IntegerField(null=False,default=0)
    rating = models.IntegerField(default=0)
    unit_in_order = models.IntegerField(default=0)
    description = models.TextField(max_length=5000,default='')
    @classmethod
    def create(cls,product_name,product_price):
        product = cls(product_name=product_name,product_price=product_price)
        return product
    @classmethod
    def get_by_product_id(cls,product_id):
        products = ProductModel.objects.filter(id=product_id).values()
        if products[:1]:
            product = products[0]
            product["images"]  = ProductImage.objects.filter(product_id=product_id).values()
            product['reviews'] = Review.find_by_product_id(product_id)
            product['sku'] = SKU.objects.filter(id=product['sku_id']).values()[0]
            return product
        else:
            return {}
    @classmethod
    def get_all_product(cls):
        products = ProductModel.objects.all()
        products = serializers.serialize('json',products)
        products = json.loads(products)
        for product in products:
            product["fields"]['images'] = ProductImage.objects.filter(product_id=product['pk']).values()
        return products