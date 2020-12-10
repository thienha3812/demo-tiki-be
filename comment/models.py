# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    account_id = models.CharField(max_length=1000000000000)
