# -*- coding: utf-8 -*-
from django.template.context_processors import request
from rest_framework import status
from rest_framework.response import Response

from ultis import response_with_error

errors  = {
    '1001' : {
        'code': 1001,
        'message': 'Vui lòng đăng nhập để tiếp tục thao tác!',
        'error': 'Token invalid',
        'status': status.HTTP_401_UNAUTHORIZED
    }
}
def check_token_valid(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if token == 'null':
            raise Exception
        else:
            return True
    except Exception as e:
        return False
def authorize_token(func):
    def wrapper(request):
        token_is_valid = check_token_valid(request)
        if not token_is_valid:
            return response_with_error(errors['1001'])
        response = func(request)
        return response
    return wrapper

