# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from _curses import raw
from strop import strip

import jwt
from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account
from middleware import authorize_token
from review.models import Review
from review.services import save_img

responses = {
    '1001': {
        'code': 1001,
        'message': 'Bình luận thành công',
        'status': status.HTTP_200_OK
    },
    '1002':{
        'code': 1002,
        'mssage': 'Bình luận thất bại',
        'status': status.HTTP_500_INTERNAL_SERVER_ERROR
    }
}

@api_view(['POST'])
@authorize_token
def create_review(request):
    token = request.META.get('HTTP_AUTHORIZATION', '')
    decode_token = jwt.decode(token, 'secret', algorithms='HS256')
    account_id = decode_token['account_id']
    body = request.POST
    comment = body['comment']
    product_id = body['product_id']
    rating_level = body['rating_level']
    review = Review.create(account_id=account_id,comment=comment,rating_level=rating_level,product_id=product_id)
    save_img(request,review_id = review.id)
    print review.id
    review = Review.find_by_id(id=review.id)
    if review is not None:
        return Response({'review':review},status=responses['1001']['status'])
    else:
        return Response(responses['1002'],status=responses['1002']['status'])