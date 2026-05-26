from django.shortcuts import render
from django.views import generic
from .models import Supplier


class ListSupplier(generic.ListView):
    model = Supplier
    template_name = 'suppliers.html'
    context_object_name = 'suppliers'
