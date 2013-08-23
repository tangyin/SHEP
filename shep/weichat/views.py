#coding-utf8

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import checkSignature

@csrf_exempt
def index(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
        return HttpResponse('Hello World')
