from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.accounts_register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]
