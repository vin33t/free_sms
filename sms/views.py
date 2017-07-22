# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SendSms
from .send_sms import send_sms


# Create your views here.
def sms(requests):
    if requests.method == "POST":
        sms = SendSms(requests.POST)
        if sms.is_valid():
            phone = sms.cleaned_data['phone']
            message = sms.cleaned_data['message']

            if send_sms(phone,message) == True:
                return render(requests, 'sms/successful.html',{'phone':phone,'message':message})
            else:
                return render(requests, 'sms/error.html',{'error':'Unable to send SMS. Please Try Again.'})

    elif requests.method == "GET":
        sms = SendSms()
        return render(requests,'sms/index.html',{'sms':sms})
