import json
import os
from operator import concat
from os import stat

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def render_image(request,img_name):
    print 123
    fp  = os.path.join('./static/images',img_name)
    with open(fp) as f:
        data = f.read()
        return HttpResponse(data,content_type='image/jpeg')