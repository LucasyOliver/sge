from django.urls import path
from .views import (
    BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView,
    CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView,
    ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView,
    BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('brands/list', BrandListView.as_view(), name='brands_list'),
    path('brands/create', BrandCreateView.as_view(), name='brands_create'),
    path('brands/<int:pk>/detail', BrandDetailView.as_view(), name='brands_detail'),
    path('brands/<int:pk>/update', BrandUpdateView.as_view(), name='brands_update'),
    path('brands/<int:pk>/delete', BrandDeleteView.as_view(), name='brands_delete'),

    path('api/v1/brands/', BrandListCreateAPIView.as_view(), name='brand-list-create-api-view'),
    path('api/v1/brands/<int:pk>', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-retrieve-update-destroy-api-view'),

    path('categories/list', CategoryListView.as_view(), name='categories_list'),
    path('categories/create', CategoryCreateView.as_view(), name='categories_create'),
    path('categories/<int:pk>/detail', CategoryDetailView.as_view(), name='categories_detail'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='categories_delete'),

    path('api/v1/categories', CategoryListCreateAPIView.as_view(), name='category-list-create-api-view'),
    path('api/v1/categories/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy-api-view'),

    path('products/list', ProductListView.as_view(), name='products_list'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/detail', ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),

    path('api/v1/products', ProductListCreateAPIView.as_view(), name='product-list-create-api-view'),
    path('api/v1/products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy-api-view'),
]
