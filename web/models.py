# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teste(models.Model):
    """(Teste description)"""
    
    name = models.TextField()
    photo = models.ImageField(upload_to="web/uploads", blank=True)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.name
