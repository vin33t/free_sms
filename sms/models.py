# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sms(models.Model):
    phone = models.CharField(max_length = 13)
    message = models.CharField(max_length = 360)