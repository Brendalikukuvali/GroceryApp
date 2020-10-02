from django.test import TestCase

# Create your tests here.from django import forms
from catalogue.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
