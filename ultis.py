from rest_framework.response import Response
from django.core.files import File as DFile

def response_with_error(error):
    data = {
        'code': error['code'],
        'error': error['error'],
        'message': error['message']
    }
    return Response(data,status=error['status'])



