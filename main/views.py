from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import requests


#@login_required()
def say_hello(request):
    return HttpResponse("Hello World")

#@login_required()
def index(request):
    filtered_requests = requests.objects.filter(requests_status_id=2)
    return render(request, 'requestList.html', {'requests': filtered_requests})
    #return render(request, 'index.html')

#@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

def request_list(request):
    return render(request, 'requesrList.html')
