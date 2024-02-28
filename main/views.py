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
from .models import CustomUser


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
    requests_pending_list = requests.objects.filter(
        Q(requests_status_id=RequestStatusId.PENDING.value) | Q(requests_status_id=RequestStatusId.NOT_DELIVERED.value))
    requests_done_list = requests.objects.filter(requests_status_id=RequestStatusId.DONE.value)
    profile = CustomUser.objects.filter(id=request.user.id)

    return render(request, 'dashboard.html',
                  {'requests_pending_list': requests_pending_list, 'requests_done_list': requests_done_list,
                   'profile': profile})


@login_required()
def history(request):
    filter_value = request.GET.get('filter')
    sort_value = request.GET.get('sort_value')
    if filter_value == "donate":
        history_request = requests.objects.filter(
            donate_user_id=request.user.id,
            requests_status_id=RequestStatusId.DONE.value
        )
        filter_history = "donate"

    elif filter_value == "received":
        history_request = requests.objects.filter(
            receive_user_id=request.user.id,
            requests_status_id=RequestStatusId.DONE.value
        )
        filter_history = "received"

    else:
        history_request = requests.objects.filter(
            Q(donate_user_id=request.user.id) | Q(receive_user_id=request.user.id),
            requests_status_id=RequestStatusId.DONE.value
        )
        filter_history = "none"

    if sort_value == "sort_down":
        history_request = history_request.order_by('date')
        sort_value = "sort_down"
    else:
        history_request = history_request.order_by('-date')
        sort_value = "sort_up"
    return render(request, 'history.html',
                  {'history_request': history_request, 'filter_history': filter_history, 'sort_value': sort_value})


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


def api(request):
    return render(request, 'api.html')