from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import  messages
 
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required

from trend.models import *
from trend.forms import *

from django.shortcuts import render
from django.contrib.auth.models import Group



def home(request):
    form= contactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = contactForm


    context ={'form':form}
    return render(request, 'index.html' , context)


# # @login_required(login_url='clicked')
# def Hire_developers(request):
#     form= CompanyForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()

#     context = {'form':form}
#     return render(request, 'Hire_developers.html', context)

