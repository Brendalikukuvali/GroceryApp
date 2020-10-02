from django.contrib import admin
from .models import Cart, Order,Payment

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
