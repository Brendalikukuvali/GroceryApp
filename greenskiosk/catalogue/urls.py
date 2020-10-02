from django.urls import path
from .views import products_list
from .models import Product
from .views import upload_product, products_details


urlpatterns = [
    path('', products_list, name='products-lists'),
    path('products/<int:product_id>/', products_details, name='products-details'),
    # path( 'products/<int:product_id>/', products_add_to_cart, name='products-add-to-cart'),
    path("products/upload/", upload_product, name="products-uploads")
    
]