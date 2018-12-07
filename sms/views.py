# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SendSmsForm
from .send_sms import send_sms
from django.http import HttpResponse,JsonResponse
import requests


# Create your views here.
def sms_view(request):
    form_class = SendSmsForm

    if request.method == "POST":
        sms = form_class(data=request.POST)
        if sms.is_valid():
            postal_code = sms.cleaned_data['postal_code']
            # message = sms.cleaned_data['message']

            if send_sms(postal_code) == True:
                request_url = ('http://api.postcodes.io/postcodes/' + postal_code)
                response = requests.get(request_url).json()
                country = response['result']['country']

                return render(request, 'sms/successful.html',{'postal_code':postal_code, 'country':country})
            else:
                return render(request, 'sms/error.html',{'error':'Unable to send SMS. Please Try Again.'})
        else:
            #form data is not valid.
            return HttpResponse("Invalid phone number or Message. Try again.")
    elif request.method == "GET":
        #sms = SendSmsForm()
        return render(request,'sms/index.html',{'form':form_class})
    else:
        #form data is not valid.
        return HttpResponse("Bad request. Try again.")

