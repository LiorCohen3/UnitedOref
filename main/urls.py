from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('dashboard/', views.dashboard),
    path('', views.request_list),
]
