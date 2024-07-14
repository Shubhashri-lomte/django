from django.contrib import admin

# Register your models here.
# service_gas_utility/admin.py

from django.contrib import admin
from .models import ServiceRequest

admin.site.register(ServiceRequest)
