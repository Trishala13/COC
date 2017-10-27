# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def zone(request):
    return render(request, 'info/zone.html', {})

def division(request):
    return render(request, 'info/division.html', {})




