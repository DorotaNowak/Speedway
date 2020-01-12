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

urlpatterns = [
    path('', home_response, name='home'),
    path('accounts/profile/', after_login_response, name='test'),
    path('teams/<int:id>', index, name='index'),
    path('create-team/', create_team, name='create'),
    path('my-teams/', my_teams, name='my-teams-name'),
    path('create-league/', create_league, name='leagues'),
    path('leagues/<int:id>', chosen_league, name='chosen_league'),
    path('my-leagues', my_leagues),
    path('join-to-league/', join_to_league),
    path('join-to-league/add-teams-to-league/<int:league_id>', add_teams_to_league, name='add-teams-to-league-name')
]
