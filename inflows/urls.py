from django.urls import path
from .views import ListInflow

urlpatterns = [
    path('inflows/list', ListInflow.as_view(), name='inflows_list'),
]