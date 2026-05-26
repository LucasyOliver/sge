from django.shortcuts import render
from django.views import generic
from .models import Outflow


class ListOutflow(generic.ListView):
    model = Outflow
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'
