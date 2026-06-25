from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView

urlpatterns = [
    path('outflows/list', OutflowListView.as_view(), name='outflows_list'),
    path('outflows/create', OutflowCreateView.as_view(), name='outflows_create'),
    path('outflows/<int:pk>/detail', OutflowDetailView.as_view(), name='outflows_detail'),
]