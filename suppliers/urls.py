from django.urls import path
from .views import ListSupplier

urlpatterns = [
    path('suppliers/list', ListSupplier.as_view(), name='suppliers_list')
]