from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import test_response
from .views import home_response
from .views import after_login_response
from .views import stats_page
from .views import ranking_page
from .views import league_page
from django.urls import path, include

urlpatterns = [
    path('accounts/profile/', after_login_response, name='test'),
    path('', home_response, name='home'),
    path('stats/', stats_page),
    path('rankings/', ranking_page),
    path('leagues/', league_page),
]

from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
