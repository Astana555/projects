# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bootstrap_page_handler, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
]