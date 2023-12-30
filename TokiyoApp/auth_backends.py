from django.contrib.auth.backends import ModelBackend
from .models import CustomerDetail

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, customerEmail=None, customerPassword=None):
        try:
            user = CustomerDetail.objects.get(customerEmail=customerEmail)
            if user.customerPassword == customerPassword:
                return user
        except CustomerDetail.DoesNotExist:
            return None
