# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=16)
    holder_name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=1000,default='')
    @classmethod
    def login(cls,email,password):
        account = Account.objects.filter(email=email,password=password).values()
        if account[:1]:
            return account[0]
        else:
            return None
