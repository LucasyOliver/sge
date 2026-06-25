from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm


class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains = product)

        return queryset


class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflows_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflows_list')


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflows_detail.html'

