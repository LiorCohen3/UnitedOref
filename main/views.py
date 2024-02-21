from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import requests
# from .Algorithm import alg



#@login_required()
def say_hello(request):
    return HttpResponse("Hello World")

#@login_required()
def index(request):
    requests_list = requests.objects.filter(requests_status_id=2).order_by('date')
    # filtered_requests = alg(filtered_requests)
    area = "North"
    type = 1
    algScore={}
    for index,request in enumerate(requests_list):
        algScore[index]=1
        if request.area == area:  #same area donation
            algScore[index]=algScore[index]+10
        elif (area=="North" and request.area=="South") or (area=="South" and request.area=="North"):   #far area donation
            algScore[index]=algScore[index]+1
        else:   #semi far area donation
            algScore[index]=algScore[index]+5

        if request.type_id==type: #type of donation matchs
            algScore[index]=algScore[index]+10
        # if request.type_id.quantityReq<=donationCap:    #he can donate more then the req
        #     algScore[index]+=5*(donationCap/request.type_id.quantityReq)
        # else:   #the amount he can is lower then the req
        #     algScore[index]-=30

        algScore[index]=algScore[index]+(10/(index+1))    #add score by the index for the request
    sorted_list = {}
    sorted_list = sorted(requests_list, key=lambda x: x.algScore, reverse=True) #order list by highest algScore
    return render(request, 'requestList.html', {'requests': sorted_list})
    #return render(request, 'index.html')

#@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

def request_list(request):
    return render(request, 'requesrList.html')
