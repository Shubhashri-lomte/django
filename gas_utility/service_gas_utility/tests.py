from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import ServiceRequest  # Import your models or other components to test

class ServiceRequestTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or state before each test method
        ServiceRequest.objects.create(
            type='Gas Connection',
            details='Need a new gas connection for my home.'
        )
        ServiceRequest.objects.create(
            type='Gas Repair',
            details='Gas stove not working properly.'
        )

    def test_service_request_creation(self):
        """Test creating a service request."""
        gas_connection = ServiceRequest.objects.get(type='Gas Connection')
        gas_repair = ServiceRequest.objects.get(type='Gas Repair')
        
        self.assertEqual(gas_connection.details, 'Need a new gas connection for my home.')
        self.assertEqual(gas_repair.details, 'Gas stove not working properly.')

    def test_service_request_count(self):
        """Test counting total service requests."""
        self.assertEqual(ServiceRequest.objects.count(), 2)

    # Add more test methods as needed
# service_gas_utility/tests.py

from django.test import TestCase
from .models import ServiceRequest

class ServiceRequestTestCase(TestCase):
    def setUp(self):
        ServiceRequest.objects.create(
            request_type='Gas Connection',
            details='Need a new gas connection for my home.'
        )
        ServiceRequest.objects.create(
            request_type='Gas Repair',
            details='Gas stove not working properly.'
        )

    def test_service_request_creation(self):
        gas_connection = ServiceRequest.objects.get(request_type='Gas Connection')
        gas_repair = ServiceRequest.objects.get(request_type='Gas Repair')

        self.assertEqual(gas_connection.details, 'Need a new gas connection for my home.')
        self.assertEqual(gas_repair.details, 'Gas stove not working properly.')

    def test_service_request_count(self):
        self.assertEqual(ServiceRequest.objects.count(), 2)
