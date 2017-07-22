from django import forms
#from .models import Sms

class SendSmsForm(forms.Form):
    phone = forms.CharField(required = True)
    message = forms.CharField(required = True, widget = forms.Textarea)
