from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('history/', views.history, name='History'),
    path('pending/', views.pending, name='Pending'),
    path('donate/', views.donation_form, name='Donation Form'),
    path('method/', views.donation_type, name='Donation Type'),
    path('pending/', views.pending, name='Pending'),
    path('edit_profile/', views.edit_profile, name='Edit Profile'),
    path('match/', views.alg_result, name='alg_result'),
    path('dashboard/', views.edit_user, name='edit_user'),
    path('api/', views.api, name='api')
]
