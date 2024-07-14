# service_gas_utility/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_request_list, name='service_request_list'),
    path('<int:pk>/', views.service_request_detail, name='service_request_detail'),
    # Add more URL patterns as needed
]
