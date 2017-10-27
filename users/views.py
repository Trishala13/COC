# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def user_site(request):
    return render(request, 'users/user_site.html', {})

def sign_in(request):
    return render(request, 'users/sign-in.html', {})

def sign_up(request):
    return render(request, 'users/sign-up.html', {})

def complaint(request):
    return render(request, 'users/complaint.html', {})

def sign_up_form(request):
	firstname=request.POST.get("firstname",None)
	lastname=request.POST.get("lastname",None)
	username=request.POST.get("username",None)
	password=request.POST.get("password",None)
	mail=request.POST.get("email",None)
	return render(request, 'users/user_site.html', {})

def sign_in_form(request):
	username=request.POST.get("username",None)
	password=request.POST.get("password",None)
	return render(request, 'users/user_site.html', {})

def complaint_form(request):
	zone=request.POST.get("zone",None)
	division=request.POST.get("division",None)
	department=request.POST.get("department",None)
	details=request.POST.get("details",None)
	return render(request, 'users/complaint.html', {})



