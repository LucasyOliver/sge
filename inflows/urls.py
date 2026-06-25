from django.urls import path
from .views import InflowListView, InflowCreateView, InflowDetailView

urlpatterns = [
    path('inflows/list', InflowListView.as_view(), name='inflows_list'),
    path('inflows/create', InflowCreateView.as_view(), name='inflows_create'),
    path('inflows/<int:pk>/detail', InflowDetailView.as_view(), name='inflows_detail'),
]