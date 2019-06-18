# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from rest_framework.authtoken.models import Token


# Create your models here.
class RegistroGpsMovil(models.Model):
    latitud           = models.CharField(max_length=200)
    longitud          = models.CharField(max_length=200)
    accuray           = models.CharField(max_length=200)
    altitude          = models.CharField(max_length=200)
    speed             = models.CharField(max_length=200)
    speed_accuracy    = models.CharField(max_length=200)
    marca_phone       = models.CharField(max_length=200,blank=True)
    sist_operativo    = models.CharField(max_length=200,blank=True)
    version           = models.CharField(max_length=200,blank=True)
    imei              = models.CharField(max_length=200,blank=True)
    mac_adress        = models.CharField(max_length=200,blank=True)
    ip_adress         = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return '%s %s %s' % (self.latitud, self.longitud, self.marca_phone)

