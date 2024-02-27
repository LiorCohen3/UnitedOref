from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('history/', views.history, name='History'),
    path('pending/', views.pending, name='Pending'),
    path('donation/', views.new_donation),
    path('', views.donation_form, name='Donation Form'),
    path('match/', views.alg_result, name='alg_result'),
]
