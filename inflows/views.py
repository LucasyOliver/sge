from django.shortcuts import render
from django.views import generic
from .models import Inflow


class ListInflow(generic.ListView):
    model = Inflow
    template_name = 'inflows_list.html'
    context_object_name = 'inflows'
