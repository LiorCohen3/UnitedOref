from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def say_hello(request):
    return HttpResponse("Hello World")

@login_required()
def index(request):
    return render(request, 'index.html')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')
