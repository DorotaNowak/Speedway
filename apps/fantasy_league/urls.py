from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import home_response
from .views import after_login_response
from .views import index
from django.urls import path
from .views import view
from .views import create
from .views import leagues
from .views import chosen_league
from .views import join_to_league

urlpatterns = [
    path('', home_response, name='home'),
    path('accounts/profile/', after_login_response, name='test'),
    path('<int:id>', index, name='index'),
    path('create/', create, name='create'),
    path('view/', view, name='view'),
    path('leagues/', leagues, name='leagues'),
    path('leagues/<int:id>', chosen_league, name='chosen_league'),
    path('join_to_league/',join_to_league)
]
