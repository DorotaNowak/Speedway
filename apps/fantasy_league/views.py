from .models import Team, Player, League
from .forms import CreateTeamForm, CreateLeagueForm, JoinLeagueForm, AddTeamToLeague
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
import hashlib
from django.contrib import messages
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def home_response(request):
    return render(request, 'join_game.html')


@login_required
def after_login_response(request):
    return render(request, 'home.html')


@login_required
def my_leagues(request):
    leagues = League.objects.filter(users__id=request.user.id)
    return render(request, 'my_leagues.html', {"leagues": leagues})


@login_required
def create_team(response):
    if response.method == "POST":
        form = CreateTeamForm(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            team = Team(name=name, player1=None, player2=None, player3=None, player4=None)
            team.save()  # save to database
            response.user.team.add(team)

        return HttpResponseRedirect("/teams/%i" % team.id)

    else:
        form = CreateTeamForm()

    return render(response, "create_team.html", {"form": form})


@login_required
def my_teams(request):
    return render(request, "my_teams.html")


@login_required
def index(response, id):
    today = date.today().strftime('%Y%m%d')
    team = Team.objects.get(id=id)
    exclude_players = []
    if team.player1 is not None:
        exclude_players.append(team.player1.id)
    if team.player2 is not None:
        exclude_players.append(team.player2.id)
    if team.player3 is not None:
        exclude_players.append(team.player3.id)
    if team.player4 is not None:
        exclude_players.append(team.player4.id)

    all_players = Player.objects.exclude(pk__in=exclude_players)
    if team in response.user.team.all() and today != '20200122':
        if response.method == "POST":
            if response.POST.get("save"):
                for item in team:
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:  # ktos kliknal dodaj zawodnika i zaznaczyl zawodnika
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player1:
                        print('bbbbbbb')
                        old_price = team.player1.price
                        # old_player_id = team.player1.id
                    if team.budget + old_price >= player.price:
                        print('aaaaaaaaaaaaaaaaaaa')
                        team.player1 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                        exclude_players.append(player.id)
                        all_players = Player.objects.exclude(pk__in=exclude_players)
                    if team.budget + old_price < player.price:
                        messages.info(response, 'Nie masz wystarczającego budżetu na zakup zawodnika: ' + str(
                            player.last_name) + ' ' + str(player.first_name))
                        print('klurwa')
                else:
                    messages.info(response, 'Nie masz wystarczającego budżetu na zakup zawodnika: ')
                    return render(response, "team.html",
                                  {"team": team, "all_players": all_players, "messages": messages})

            elif response.POST.get("newItem2"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player2:
                        old_price = team.player2.price
                        old_player_id = team.player2.id
                    if team.budget + old_price >= player.price:
                        team.player2 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                        exclude_players.append(player.id)
                        all_players = Player.objects.exclude(pk__in=exclude_players)
                else:
                    print("invalid")

            elif response.POST.get("newItem3"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player3:
                        old_price = team.player3.price
                        old_player_id = team.player3.id
                    if team.budget + old_price >= player.price:
                        team.player3 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                        exclude_players.append(player.id)
                        all_players = Player.objects.exclude(pk__in=exclude_players)
                else:
                    print("invalid")

            elif response.POST.get("newItem4"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player4:
                        old_price = team.player4.price
                        old_player_id = team.player4.id
                    if team.budget + old_price >= player.price:
                        team.player4 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                        exclude_players.append(player.id)
                        all_players = Player.objects.exclude(pk__in=exclude_players)
                else:
                    print("invalid")
            team.score = team.count_score()
            team.save()

        return render(response, "team.html", {"team": team, "all_players": all_players})

    return render(response, "blocked_team.html", {"team": team})


@login_required
def join_to_league(response):
    all_leagues = League.objects.all()  # return all leagues
    if response.method == "POST":
        form = JoinLeagueForm(response.POST)

        if form.is_valid():
            print("valid")
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            all_leagues = [a.name for a in all_leagues]
            if name not in all_leagues:
                return render(response, "join_to_league.html")
            h = hashlib.new('ripemd160')
            h.update(bytes(password, encoding='utf-8'))

            if h.hexdigest() == League.objects.get(name=name).password:
                league = League.objects.get(name=name)
                league_id = league.id
                league.users.add(response.user)
                print(league_id)
                return HttpResponseRedirect("/leagues/add-teams/%i" % league_id)
                # return HttpResponseRedirect(reverse("add-teams-to-league-name"), {"league_id":league_id})

        else:
            return render(response, "join_to_league.html")
    else:
        form = JoinLeagueForm()
    return render(response, 'join_to_league.html', {"all_leagues": all_leagues, "form": form})


@login_required
def add_teams_to_league(response, league_id):
    if response.method == "POST":
        user_teams = response.user.team.all()
        user_team_names = [team.name for team in user_teams]
        form = AddTeamToLeague(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name in user_team_names:
                league = League.objects.get(id=league_id)
                league.teams.add(Team.objects.get(name=name))
                return HttpResponseRedirect("/leagues/add-teams/%i" % league_id)
        else:
            return HttpResponseRedirect("/leagues/add-teams/%i" % league_id)
    else:
        form = AddTeamToLeague()
    return render(response, "add_team_to_league.html", {"form": form})


@login_required
def create_league(response):
    if response.method == "POST":
        form = CreateLeagueForm(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if password == confirm_password:
                h = hashlib.new('ripemd160')
                h.update(bytes(password, encoding='utf-8'))

                league = League(name=name, password=h.hexdigest())
                league.save()
                league.users.add(response.user)
                return HttpResponseRedirect(reverse('test'))
            else:
                return render(response, 'create_league.html', {"form": form})

    else:
        form = CreateLeagueForm()

    return render(response, "create_league.html", {"form": form})


@login_required
def chosen_league(response, id):
    league = League.objects.get(id=id)
    teams_in_league = Team.objects.filter(league=id).order_by('score').reverse()
    return render(response, 'league.html', {"teams": teams_in_league, "league": league})
