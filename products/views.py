from django.shortcuts import render
from django.views import generic
from .models import Product


class ListProduct(generic.ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    
