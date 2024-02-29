import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DonationForm
from .forms import EditProfileForm
from .request import RequestStatusId
from .algorithm import alg
from .models import requests
from .models import CustomUser
from .models import unit_img


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
            requests_list = requests.objects.filter(requests_status=RequestStatusId.PENDING.value).select_related(
                'requests_status', 'item_type').all()
            sorted_requests = alg(requests_list, auto_match, area, donation_type, item_type)
            return render(request, 'request_list.html', {'requests': sorted_requests, 'form': form})
    else:
        form = DonationForm()
    return render(request, 'request_list.html', {'form': form})


@login_required()
def dashboard(request):
    requests_pending_list = requests.objects.filter(
        Q(requests_status=RequestStatusId.PENDING.value) | Q(requests_status=RequestStatusId.NOT_DELIVERED.value))[:5]
    requests_done_list = requests.objects.filter(requests_status=RequestStatusId.DONE.value)[:5]
    profile = CustomUser.objects.get(id=request.user.id)
    unit = unit_img.objects.get(unit_name=profile.unit)

    return render(request, 'dashboard.html',
                  {'requests_pending_list': requests_pending_list, 'requests_done_list': requests_done_list,
                   'profile': profile, 'unit': unit})


@login_required()
def history(request):
    filter_value = request.GET.get('filter')
    sort_value = request.GET.get('sort_value')
    if filter_value == "donate":
        history_request = requests.objects.filter(
            donate_user=request.user.id,
            requests_status=RequestStatusId.DONE.value
        )
        filter_history = "donate"

    elif filter_value == "received":
        history_request = requests.objects.filter(
            donate_user=request.user.id,
            requests_status=RequestStatusId.DONE.value
        )
        filter_history = "received"

    else:
        history_request = requests.objects.filter(
            Q(donate_user=request.user.id) | Q(requestor=request.user.id),
            requests_status=RequestStatusId.DONE.value
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
        Q(donate_user=request.user.id) | Q(requestor=request.user.id),
        Q(requests_status=RequestStatusId.PENDING.value) | Q(requests_status=RequestStatusId.NOT_DELIVERED.value)
    )

    return render(request, 'pending.html', {'pending_list': pending_list})


@login_required()
def request_list(request):
    return render(request, 'requestList.html')


@login_required()
def new_donation(request):
    return render(request, 'NewDonation.html')


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            # Assuming you have a User model, update the user details here
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.phone = form.cleaned_data['phone']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            flag = True
            #
            messages.success(request, 'User information updated successfully.')
            return redirect('Dashboard')

    form = EditProfileForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phone': request.user.phone,
        'email': request.user.email,
    })

    return render(request, 'edit_profile.html', {'form': form})


@login_required()
def api(request):
    return render(request, 'api.html')


@login_required()
def edit_user(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            # Assuming you have a User model, update the user details here
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.phone = form.cleaned_data['phone']
            request.user.email = form.cleaned_data['email']
            request.user.save()

            messages.success(request, 'User information updated successfully.')
            return redirect('dashboard')

        else:
            form = EditProfileForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'phone': request.user.phone,
                'email': request.user.email,
            })

        return render(request, 'edit_user.html', {'form': form})
