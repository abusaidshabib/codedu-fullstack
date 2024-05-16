from django.urls import path
from . import views
from . import urls

urlpatterns = [
    path('', views.DashboardView.as_view(), name='admin_dashboard'),
    path('blogs/', views.DashboardView.as_view(), name='add_blogs'),
    path('add-category/', views.DashboardView.as_view(), name='add_category')
]