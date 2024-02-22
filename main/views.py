from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .request import RequestStatusId
from .algorithm import alg
from .models import requests


# @login_required()
def say_hello(request):
    return HttpResponse("Hello World")


@login_required()
def index(request):
    requests_list = requests.objects.filter(requests_status_id=RequestStatusId.PENDING.value)
    area = "North"
    item_type = 1
    sorted_requests = alg(requests_list, True, area, item_type)
    return render(request, 'request_list.html', {'requests': sorted_requests})


# @login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


def request_list(request):
    return render(request, 'requesrList.html')
