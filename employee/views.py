# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def official_login(request):
    return render(request, 'employee/official-login.html', {})

def emp_site(request):
    return render(request, 'employee/employee_site.html', {})

def official_login_form(request):
    emp_id=request.POST.get("empid",None)
    password=request.POST.get("password",None)
    return render(request, 'employee/employee_site.html', {})


