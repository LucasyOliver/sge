from django.urls import path
from .views import ListProduct

urlpatterns = [
    path('products/list', ListProduct.as_view(), name='products_list')
]