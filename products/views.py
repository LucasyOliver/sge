from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product, Brand, Category
from .forms import BrandForm


class BrandListView(ListView):
    model = Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains = name)

        return queryset


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brands_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brands_detail.html'


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brands_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brands_delete.html'
    success_url = reverse_lazy('brands_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
