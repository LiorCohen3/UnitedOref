from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DonationForm
from .forms import EditProfileForm
from .forms import NewRequest
from .request import RequestStatusId
from .algorithm import alg
from .models import requests
from .models import CustomUser
from .models import unit_img
from .models import item_type


@login_required()
def donation_form(request):
    form = DonationForm()
    return render(request, 'donation_form.html', {'form': form})


@login_required()
def donation_type(request):
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == 'option1':
            return redirect('Donation Form')
        elif option == 'option2':
            return redirect('Manual Donation')
    return render(request, 'donation_type.html')


@login_required()
def alg_result(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            item_type = form.cleaned_data['item_type']
            donation_type = form.cleaned_data['donation_type']
            count = form.cleaned_data['count']
            requests_list = requests.objects.filter(requests_status=RequestStatusId.PENDING.value).select_related(
                'requests_status', 'item_type').all()
            if not requests_list:
                messages.info(request, 'Good news! There are currently no open requests.')
                return redirect('Dashboard')
            sorted_requests = alg(requests_list, area, item_type, count, donation_type)
            return render(request, 'request_list.html', {'requests': sorted_requests, 'form': form})
    else:
        form = DonationForm()
    return render(request, 'request_list.html', {'form': form})


@login_required()
def dashboard(request):
    requests_pending_list = requests.objects.filter(
        Q(requests_status=RequestStatusId.PENDING.value) | Q(requests_status=RequestStatusId.NOT_DELIVERED.value)).order_by('-date')[:5]
    requests_done_list = requests.objects.filter(requests_status=RequestStatusId.DONE.value).order_by('-date')[:5]
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
            donate_user_id=request.user.id,
            requests_status_id=RequestStatusId.DONE.value
        )
        filter_history = "donate"
    elif filter_value == "received":
        history_request = requests.objects.filter(
            requestor_id=request.user.id,
            requests_status_id=RequestStatusId.DONE.value
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
    user_id = request.user.id
    return render(request, 'pending.html', {'pending_list': pending_list, "user_id": user_id})


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


@login_required()
def request_form(request):
    return render(request, 'request_form.html')


@login_required()
def request_form(request):
    if request.method == 'POST':
        form = NewRequest(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            area = form.cleaned_data['area']
            info = form.cleaned_data['info']
            item_quantity = form.cleaned_data['item_quantity']
            requestor = request.user
            requests.objects.create(item_name=item_name, area=area, info=info, item_quantity=item_quantity, requestor=requestor)
            return render(request, 'request_form.html', {'form': form})
    else:
        form = NewRequest()
        return render(request, 'request_form.html', {'form': form})