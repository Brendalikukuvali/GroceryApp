from django.db import models
from catalogue.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=60)
    basket = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer =models.ForeignKey("self", on_delete=models.CASCADE)
    payment= models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='+') 
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.customer()

class Payment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return self.order()