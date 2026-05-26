from django.urls import path
from .views import ListOutflow

urlpatterns = [
    path('outflows/list', ListOutflow.as_view(), name='outflows_list')
]