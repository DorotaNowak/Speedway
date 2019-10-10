from django.contrib import admin
from django.urls import path
from .views import test_response
urlpatterns = [
   path('test/',test_response,name='test')
]
