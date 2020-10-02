from django.contrib import admin
from .models import Product,ProductCategory,ProductReview,ProductSupplier,Product

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductSupplier)
admin.site.register(ProductReview)
