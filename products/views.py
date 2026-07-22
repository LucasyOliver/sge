from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product, Brand, Category
from .forms import BrandForm, CategoryForm, ProductForm


# SESSION CLASS BRANDS
class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'products.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains = name)

        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brands_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')
    permission_required = 'products.add_brand'
    


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brands_detail.html'
    permission_required = 'products.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brands_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')
    permission_required = 'products.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brands_delete.html'
    success_url = reverse_lazy('brands_list')
    permission_required = 'products.delete_brand'


# SESSION CLASS CATEGORIES
class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = 'products.view_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains = name)

        return queryset
    

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'categories_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')
    permission_required = 'products.add_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'categories_detail.html'
    permission_required = 'products.view_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brands_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')
    permission_required = 'products.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('categories_list')
    permission_required = 'products.delete_category'


# SESSION CLASS PRODUCTS
class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        if title:
            queryset = queryset.filter(title__icontains = title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains = serie_number)

        if brand:
            queryset = queryset.filter(brand__id = brand)

        if category:
            queryset = queryset.filter(category__id = category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'products_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'products_detail.html'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products_detail.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products_delete.html'
    success_url = reverse_lazy('products_list')
    permission_required = 'products.delete_product'
