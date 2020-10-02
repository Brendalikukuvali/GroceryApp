from django.shortcuts import render,redirect
from .forms import ProductForm

# Create your views here.

from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render (request, 'products_lists.html', {'products': products})

def products_details(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'products_details.html', {'products': products})

# def add_to_cart(request):
#     products = product.objects.all()
#     return render(request, 'products_add_to_cart.html', {'products':products})
  

def upload_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products-lists')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

