from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowListCreateAPIView


urlpatterns = [
    path('outflows/list', OutflowListView.as_view(), name='outflows_list'),
    path('outflows/create', OutflowCreateView.as_view(), name='outflows_create'),
    path('outflows/<int:pk>/detail', OutflowDetailView.as_view(), name='outflows_detail'),

    path('api/v1/outflows', OutflowListCreateAPIView.as_view(), name='outflow-list-create-api-view'),
]
