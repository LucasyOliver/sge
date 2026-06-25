from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product, Brand, Category
from .forms import BrandForm, CategoryForm, ProductForm


# SESSION CLASS BRANDS
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


# SESSION CLASS CATEGORIES
class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains = name)

        return queryset
    

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories_detail.html'


class CategoryUpdateView(UpdateView):
    model = Brand
    template_name = 'brands_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('categories_list')


# SESSION CLASS PRODUCTS
class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        if title:
            queryset = queryset.filter(title__icontains = title)

        if serie_number:
            queryset = queryset.filter(serie_number__icointains = serie_number)

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


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products_detail.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products_delete.html'
    success_url = reverse_lazy('products_list')