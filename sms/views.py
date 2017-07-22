# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SendSmsForm
from .send_sms import send_sms
from django.http import HttpResponse

# Create your views here.
def sms_view(request):
    form_class = SendSmsForm

    if request.method == "POST":
        sms = form_class(data=request.POST)
        if sms.is_valid():
            phone = sms.cleaned_data['phone']
            message = sms.cleaned_data['message']

            if send_sms(phone,message) == True:
                return render(request, 'sms/successful.html',{'phone':phone,'message':message})
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

