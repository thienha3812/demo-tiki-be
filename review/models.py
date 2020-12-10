# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uu
from uuid import uuid4

from django.core.files.storage import FileSystemStorage
from django.utils import timezone

from django.db import models

# Create your models here.
from account.models import Account


class Review(models.Model):
    account_id = models.IntegerField(null=False)
    comment = models.CharField(max_length=3000)
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    rating_level = models.IntegerField()
    product_id = models.IntegerField(default=0)
    @classmethod
    def create(cls,**kwargs):
        try:
            account_id = kwargs['account_id']
            comment = kwargs['comment']
            product_id = kwargs['product_id']
            rating_level = kwargs['rating_level']
            review = cls(account_id=account_id, comment=comment, rating_level=rating_level, product_id=product_id)
            review.save()
            return review
        except Exception as e:
            return None
    @classmethod
    def find_by_product_id(cls,product_id):
        reviews = Review.objects.filter(product_id=product_id).values()
        if reviews[::]:
            for review in reviews:
                review["account"] = Account.objects.filter(id=review['account_id']).values()[0]
                review['img_review'] = ImageReview.objects.filter(review_id=review['id']).values()  
            return reviews
        else:
            return []
    @classmethod
    def find_by_id(cls,id):
        review = Review.objects.filter(id=id).values()[0]
        if review:
            review['account'] = Account.objects.filter(id=review['account_id']).values()[0]
            review['img_review'] = ImageReview.objects.filter(review_id=review['id']).values()
            return review
        else:
            return None
class ImageReview(models.Model):
    img_src = models.CharField(max_length=2000)
    type = models.CharField(max_length=100)
    size = models.IntegerField()
    review_id = models.IntegerField()
    @classmethod
    def create(cls,review_id,img):
        try:
            fs = FileSystemStorage()
            uuid = uuid4()
            file_name, file_extension = os.path.splitext(img.name)
            fp = os.path.join('./static/images/', str(uuid.hex) + file_extension)
            fs.save(fp, img)
            image = cls(img_src='static/images/' + str(uuid.hex) + file_extension, size=1, type=file_extension,
                        review_id=review_id)
            image.save()
            return image
        except Exception as e:
            return None