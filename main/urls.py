from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('history/', views.history, name='History'),
    path('history filter by date/', views.history_filter_by_date, name='history_filter_by_date'),
    path('history filter donate/', views.history_filter_donate, name='history_filter_donate'),
    path('history filter received/', views.history_filter_received, name='history_filter_received'),
    path('pending/', views.pending, name='Pending'),
    path('donation/', views.new_donation),
    path('', views.donation_form, name='Donation Form'),
    path('match/', views.alg_result, name='alg_result'),
    path('api/', views.api, name='api')
]
