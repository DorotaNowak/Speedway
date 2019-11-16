from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import test_response
from .views import home_response
from .views import after_login_response
from .views import index
from django.urls import path, include
from .views import view
from .views import home
from .views import create
urlpatterns = [
    path('', home_response, name='home'),
    path('accounts/profile/', after_login_response, name='test'),
    path('<int:id>',index,name='index'),
    path('create/',create,name='create'),
    path('home/',home,name='home'),
    path('view/',view,name='view')

]
