from django.urls import path
from .views import home_response
from .views import after_login_response
from .views import index
from .views import my_teams
from .views import create_team
from .views import create_league
from .views import chosen_league
from .views import join_to_league
from .views import add_teams_to_league
from .views import my_leagues

from django.conf.urls import url,include
from rest_framework import routers
from .views import UserViewSet
router=routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('', home_response, name='home'),
    path('accounts/profile/', after_login_response, name='test'),
    path('teams/<int:id>', index, name='index'),
    path('teams/new/', create_team, name='create'),
    path('teams/', my_teams, name='my-teams-name'),
    path('leagues/new/', create_league, name='leagues'),
    path('leagues/<int:id>', chosen_league, name='chosen_league'),
    path('leagues/', my_leagues),
    path('leagues/join/', join_to_league),
    path('leagues/add-teams/<int:league_id>', add_teams_to_league, name='add-teams-to-league-name'),
    url(r'^',include(router.urls))
]
