from django.shortcuts import render
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json
# Create your views here.

@csrf_exempt
def addMessage(request):
    if request.method=='POST':
        print('11111')
        print(request.POST)
        data = json.loads(request.body.decode('utf-8'))

        fullName = data['fullName']
        email = data['email']
        message = data['message']
        print(fullName)
        print(email)
        print(message)
        print('11111')
        m = Message(fullName=fullName, email=email, message=message)
        m.save()
        print('ok')
        return HttpResponse('Ok')