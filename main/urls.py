from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import test_response
from .views import home_response
from .views import after_login_response
from .views import league_page
from .views import stats_page
from .views import ranking_page

urlpatterns = [
   path('accounts/profile/',after_login_response,name='test'),
   path('',home_response,name='home'),
   path('accounts/profile/leagues.html',league_page),
   path('accounts/profile/stats.html',stats_page),
   path('accounts/profile/rankings.html',ranking_page),
]

from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

