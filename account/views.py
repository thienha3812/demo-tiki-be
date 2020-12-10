# -*- coding: utf-8 -*-
import json

import jwt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account
from product.models import ProductModel
from rest_framework import status
from django.core import serializers
@api_view(['POST'])
def login_account(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            email = body['email']
            password = body['password']
            account = Account.login(email,password)
            if account is not None:
                account_info = {
                    "holder_name":u''.join(account["holder_name"]).encode('utf8',errors='ignore')
                }
                token = jwt.encode({'account_id':account['id']},'secret',algorithm='HS256')
                return Response({'token':token,"message":"Đăng nhập thành công","success":True,"account_info":account_info})
            else:
                return Response({"message":"Đăng nhập thất bại","success":False})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

