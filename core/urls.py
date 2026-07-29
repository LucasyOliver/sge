from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('api/v1', include('authentication.urls')),
    path('', home, name='home'),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
    path('', include('suppliers.urls'))
]
