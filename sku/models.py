# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SKU(models.Model):
    sku_name = models.TextField()
    sku_avatar = models.TextField(default='')