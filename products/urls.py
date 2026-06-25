from django.urls import path
from .views import (
    BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView,
    CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView,
    ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('brands/list', BrandListView.as_view(), name='brands_list'),
    path('brands/create', BrandCreateView.as_view(), name='brands_create'),
    path('brands/<int:pk>/detail', BrandDetailView.as_view(), name='brands_detail'),
    path('brands/<int:pk>/update', BrandUpdateView.as_view(), name='brands_update'),
    path('brands/<int:pk>/delete', BrandDeleteView.as_view(), name='brands_delete'),

    path('categories/list', CategoryListView.as_view(), name='categories_list'),
    path('categories/create', CategoryCreateView.as_view(), name='categories_create'),
    path('categories/<int:pk>/detail', CategoryDetailView.as_view(), name='categories_detail'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='categories_delete'),

    path('products/list', ProductListView.as_view(), name='products_list'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/detail', ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
]