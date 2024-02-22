from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import DonationForm
from .request import RequestStatusId
from .algorithm import alg
from .models import requests


# @login_required()
def say_hello(request):
    return HttpResponse("Hello World")


@login_required()
def donation_form(request):
    form = DonationForm()
    return render(request, 'donation_form.html', {'form': form})


@login_required()
def alg_result(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            item_type = form.cleaned_data['item_type']
            donation_type = form.cleaned_data['donation_type']
            count = form.cleaned_data['count']
            auto_match = form.cleaned_data['auto_match']
            requests_list = requests.objects.filter(requests_status_id=RequestStatusId.PENDING.value)
            sorted_requests = alg(requests_list, auto_match, area, donation_type, item_type)
            return render(request, 'request_list.html', {'requests': sorted_requests, 'form': form})
    else:
        form = DonationForm()
    return render(request, 'request_list.html', {'form': form})


# @login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


def request_list(request):
    return render(request, 'requesrList.html')

def new_donation(request):
    return render(request, 'NewDonation.html')