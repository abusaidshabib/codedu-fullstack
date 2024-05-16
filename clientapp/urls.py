from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='main_home'),
    path('categories/', views.CategoriesView.as_view(), name='main_categories'),
    path('about/', views.AboutView.as_view(), name='main_about'),
    path('blog/', views.BlogView.as_view(), name='main_blog'),
    path('faq/', views.FaqView.as_view(), name='main_faq'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegisterView.as_view(), name='register'),
]
