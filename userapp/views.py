# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db import models
from django.http import HttpResponse
from .models import *

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request,'userapp/register.html')
    else:
        uname = request.POST.get('uname','')
        uemail = request.POST.get('uemail','')
        pwd = request.POST.get('pwd','')

        if uname and uemail and pwd:
            userapp = Register(username = uname, password = pwd, email=uemail)

            userapp.save()
            return HttpResponse('yes')
        return HttpResponse('yes')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = auth.authenticate(username = uname, password = pwd)
        if user is not None:
            auth.login(request, user)
            return HttpResponse('yes')
        else:
            return HttpResponse('no')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)

def home(request):
    return render(request,'home/index.html')


		#name = request.POST.get('name')
		#email = request.POST.get('email')
		#password = request.POST.get('password')
		#if not all([name, email, password]):
		#	return render(request,'userapp/register.html',{'errmsg':'incomplete data'})
		#userProfile.objects.create(name=username,email=email,password=password)
		#user.is_active= 0
		#user.save()
		#return render(request, 'home')


#def register_message(request):
#	rname = request.GET('username')
#	uer = UserProfile.objects.filter(name=username).first()
#	if user:
#		return JsonResponse('msg':'the name already used')
#	else:
#		return JsonResponse({'statics':'succes'})
#def login(request):
#	name = request.POST.get('name')
#	password = request.POST.get('password')

	
#	user = authenticate(request,name=name, password=password)

#	if user is not None:
#		login(request, user)
#		return redirect('home/base')
#	else:
#		messages.info(request, 'Username or password is incorect')