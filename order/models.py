# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField


# Create your models here.
from django.db import models

from product.models import ProductModel


class Order(models.Model):
    account_id = models.IntegerField()
    product_in_order = models.TextField()
    address = models.TextField()
    @classmethod
    def create(cls,**kwargs):
        try:
            account_id = kwargs['account_id']
            address = kwargs['address']
            item_in_order = json.dumps(kwargs['item_in_order'])
            order = cls(account_id=account_id, address=address, product_in_order=item_in_order)
            order.save()
            return order
        except Exception as e:
            return None
