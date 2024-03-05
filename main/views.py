from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DonationForm
from .forms import EditProfileForm
from .forms import NewRequest
from .forms import LocationForm
from .request import RequestStatusId
from .algorithm import alg
from .models import requests
from .models import item_type
from .models import CustomUser
from .models import unit_img
import os
from .models import item_type
from django.http import JsonResponse


@login_required()
def donation_form(request):
    form = DonationForm()
    return render(request, 'donation_form.html', {'form': form})


@login_required()
def donation_type(request):
    return render(request, 'donation_type.html')


@login_required()
def manual_donation(request, item_types=None):
    sort_value = request.GET.get('sort_value')
    sort_direction = request.GET.get('sort_direction', 'down')
    filters = request.GET.getlist('filter')  # Get multiple filter values if provided

    areas = ['North', 'Center', 'South']
    type_names = ['Equipment', 'Food']
    item_types_list = ['Warm Food', 'Dry Food', 'Snacks', 'Winter Clothing', 'Summer Clothing', 'Underwear', 'Socks',
                       'Tactical Vests', 'Tactical Gloves', 'Tactical Uniform', 'Tactical Boots', 'Tactical Protection',
                       'Tactical Helmets']
    units = ['Kfir', 'Givati', 'Golani', 'Nahal', 'Shiryon', 'Totchanim', 'Handasa Kravit', 'Tzanchanim',
             'Arayot Hayarden', 'Bardelas', 'Karakal', 'Chilutz Vehatzala', 'Hagana Avirit', 'Chovlim Snapear',
             'Mishmar Hagvul', 'Isuf Kravi', 'UnitedOref']

    # Fetch all requests
    requests_list = requests.objects.filter(requests_status=RequestStatusId.PENDING.value)

    # Apply sorting
    if sort_value == 'date':
        requests_list = requests_list.order_by('date') if sort_direction == 'down' else requests_list.order_by('-date')
    filtered_requests = []
    # Apply filters
    for filter_value in filters:
        if "area_" in filter_value:
            filter_value = filter_value.replace("area_", "")
            filtered_requests += requests_list.filter(area=filter_value)  # Filter by donate area
        elif "type_" in filter_value:
            filter_value = filter_value.replace("type_", "")
            don_type = 1 if filter_value == 'Food' else 2
            filtered_requests += requests_list.filter(type_id=don_type)  # Filter by received area
        elif "unit_" in filter_value:
            filter_value = filter_value.replace("unit_", "")
            filtered_requests += requests_list.filter(unit=filter_value)  # Filter by type
        elif "item_" in filter_value:
            filter_value = filter_value.replace("item_", "")
            item = item_type.objects.filter(description=filter_value)
            filtered_requests += requests_list.filter(item_type=item[0])  # Filter by item type

    return render(request, 'manual_donation.html', {
        'requests': filtered_requests or requests_list,
        'sort_value': sort_value,
        'filters': filters,
        'areas': areas,
        'type_names': type_names,
        'item_types': item_types_list,
        'units': units
    })


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
        Q(requests_status=RequestStatusId.PENDING.value) | Q(
            requests_status=RequestStatusId.NOT_DELIVERED.value)).order_by('-date')[:5]
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
def location_form(request, id):
    return render(request, 'location_form.html', {'id': id})


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
            unit = request.user.unit
            the_item_itself = item_type.objects.get(description=item_name)
            type_id = the_item_itself.item_type_id
            request_type = the_item_itself.request_type
            created_object = requests.objects.create(item_name=item_name, area=area, info=info,
                                                     item_quantity=item_quantity, requestor=requestor,
                                                     item_type_id=request_type, unit=unit, type_id=type_id)
            created_object = requests.objects.create(item_name=item_name, area=area, info=info, item_quantity=item_quantity, requestor=requestor, item_type_id=request_type, type_id=type_id)
            render(request, 'request_form.html', {'form': form})
            this_id = created_object.requests_id
            return redirect('Location Form', id=this_id)
    else:
        form = NewRequest()
        return render(request, 'request_form.html', {'form': form})


@login_required()
def location_form(request, id):
    g_api = os.environ.get("GOOGLE_API")
    location_obj = get_object_or_404(requests, requests_id=id)
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['location_lat']
            lng = form.cleaned_data['location_long']
            location_obj.location_lat = lat
            location_obj.location_long = lng
            location_obj.schedule_date = form.cleaned_data['schedule_date']
            location_obj.schedule_time = form.cleaned_data['schedule_time']
            location_obj.save()
            return redirect('Dashboard')
    else:
        print("else")
        form = LocationForm()
        return render(request, 'location_form.html', {'form': form, 'g_api': g_api})
