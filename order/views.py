# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from audioop import add
from os import stat
from uu import decode

import jwt
from django.shortcuts import render

# Create your views here.


# -*- coding: utf-8 -*-
from django.template.context_processors import request
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from middleware import authorize_token
from order.models import Order
from product.models import ProductModel
from rest_framework import status
from django.core import serializers

from ultis import response_with_error

errors  = {
    '1001' : {
        'code': 1001,
        'message': 'Vui lòng đăng nhập để tiếp tục thao tác!',
        'error': 'Token invalid',
        'status': status.HTTP_401_UNAUTHORIZED
    }
}
@api_view(['POST'])
@authorize_token
def place_order(request):
    try:
        body = json.loads(request.body)
        token = request.META.get('HTTP_AUTHORIZATION','')
        decode_token = jwt.decode(token,'secret',algorithms='HS256')
        item_in_order =  body['item_in_order']
        address = body['address']
        account_id = decode_token['account_id']
        print 'start'
        order = Order.create(item_in_order=item_in_order,address=address,account_id=account_id)
        print 'end'
        if order is not None:
            data = {
                'message': 'Đặt hàng thành công',
                'success': True
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            raise Exception
    except Exception as e:
        data = {
            'message': 'Đặt hàng thất bại',
            'success': False
        }
        return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


