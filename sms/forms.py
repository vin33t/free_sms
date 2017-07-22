from django import forms
from .models import Sms

class SendSms(forms.ModelForm):
    class Meta:
        model = Sms
        fields = ['phone','message']