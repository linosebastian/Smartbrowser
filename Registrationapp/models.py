# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    key=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

