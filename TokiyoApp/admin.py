from django.contrib import admin
from .models import *

admin.site.register(ProductDetail)
admin.site.register(CustomerDetail)
admin.site.register(CustomerAddressDetail)
admin.site.register(ProductImage)
admin.site.register(CartDetail)
admin.site.register(OrderDetail)
admin.site.register(OrderDetailsProduct)
