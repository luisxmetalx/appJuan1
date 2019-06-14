# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from rest_framework.authtoken.models import Token

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Coodenada(models.Model):
    latitud     = models.CharField(max_length=200)
    longitud    = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s %s' % (self.latitud, self.longitud)

