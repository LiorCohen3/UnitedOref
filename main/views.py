from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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


@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required()
def history(request):
    history_request = requests.objects.filter(
        Q(donate_user_id=request.user.id) | Q(receive_user_id=request.user.id),
        requests_status_id=RequestStatusId.DONE.value
    )
    filter_history = "none"
    return render(request, 'history.html', {'history_request': history_request, 'filter_history': filter_history})


@login_required()
def history_filter_by_date(request):
    history_request = requests.objects.filter(
        Q(donate_user_id=request.user.id) | Q(receive_user_id=request.user.id),
        requests_status_id=RequestStatusId.DONE.value
    ).order_by('-date')
    filter_history = "date"

    return render(request, 'history.html', {'history_request': history_request, 'filter_history': filter_history})


@login_required()
def history_filter_donate(request):
    history_request = requests.objects.filter(
        donate_user_id=request.user.id,
        requests_status_id=RequestStatusId.DONE.value
    )
    filter_history = "donate"

    return render(request, 'history.html', {'history_request': history_request, 'filter_history': filter_history})


@login_required()
def history_filter_received(request):
    history_request = requests.objects.filter(
        receive_user_id=request.user.id,
        requests_status_id=RequestStatusId.DONE.value
    )
    filter_history = "received"

    return render(request, 'history.html', {'history_request': history_request, 'filter_history': filter_history})


@login_required()
def pending(request):
    pending_list = requests.objects.filter(
        Q(donate_user_id=request.user.id) | Q(receive_user_id=request.user.id),
        Q(requests_status_id=RequestStatusId.PENDING.value) | Q(requests_status_id=RequestStatusId.NOT_DELIVERED.value)
    )

    return render(request, 'pending.html', {'pending_list': pending_list})


@login_required()
def request_list(request):
    return render(request, 'requesrList.html')


@login_required()
def new_donation(request):
    return render(request, 'NewDonation.html')
