from django.shortcuts import render

# Create your views here.
# service_gas_utility/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_gas_utility/request_list.html', {'requests': requests})

@login_required
def service_request_detail(request, pk):
    request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'service_gas_utility/request_detail.html', {'request': request})

# Add more views for creating, updating, and deleting service requests as needed.
# views.py

from django.shortcuts import render
from .models import ServiceRequest

def service_request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_gas_utility/request_list.html', {'requests': requests})

def service_request_detail(request, pk):
    request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'service_gas_utility/request_detail.html', {'request': request})
