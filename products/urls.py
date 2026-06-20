from django.urls import path
from .views import ProductListView, BrandListView, CategoryListView, BrandCreateView, BrandDetailView, BrandUpdateView

urlpatterns = [
    path('brands/list', BrandListView.as_view(), name='brands_list'),
    path('brands/create', BrandCreateView.as_view(), name='brands_create'),
    path('brands/<int:pk>/detail', BrandDetailView.as_view(), name='brands_detail'),
    path('brands/<int:pk>/update', BrandUpdateView.as_view(), name='brands_update'),
    path('categories/list', CategoryListView.as_view(), name='categories_list'),
    path('products/list', ProductListView.as_view(), name='products_list')
]