from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('dashboard/', views.dashboard),
    path('', views.donation_form, name='Donation Form'),
    path('match/', views.alg_result, name='alg_result'),
]
