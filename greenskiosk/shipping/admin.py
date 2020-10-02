from django.contrib import admin
from .models import ShippingProvider, CoolerBox, Delivery

# Register your models here.
admin.site.register(ShippingProvider)
admin.site.register(CoolerBox)
admin.site.register(Delivery) 
