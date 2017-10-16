# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Teste

# Create your views here.
def index(request):
    return render(request, 'teste.html', {'models': Teste.objects.all()})