# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from account.views import login_account
from image.views import render_image
from order.views import place_order
from product.views import get_all_product , insert_product, product_api_view
from review.views import create_review

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Product api
    url('api/product/get-all', get_all_product),
    url('api/product/insert-product', insert_product),
    url('api/product/(?P<product_id>\d+)',product_api_view),
    # Image api
    url('api/static/images/(?P<img_name>\w+.\w+)', render_image),
    # Account api
    url('api/account/login',login_account),
    # Order api
    url('api/order/place',place_order),
    # Review
    url('api/review/create',create_review)

]
