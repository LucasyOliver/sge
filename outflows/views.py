from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm
from .serializers import OutflowSerializer


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains = product)

        return queryset


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflows_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflows_list')
    permission_required = 'outflows.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflows_detail.html'
    permission_required = 'outflows.view_outflow'


class OutflowListCreateAPIView(ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

