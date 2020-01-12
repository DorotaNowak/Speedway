from .models import Team, Player, League
from .forms import CreateTeamForm, CreateLeagueForm, JoinLeagueForm, AddTeamToLeague
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date
import hashlib


def home_response(request):
    return render(request, 'login.html')


@login_required
def after_login_response(request):
    return render(request, 'home.html')


@login_required
def create(response):
    if response.method == "POST":
        form = CreateTeamForm(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            team = Team(name=name, budget=5.0, player1=None, player2=None, player3=None, player4=None)
            team.save()  # save to database
            response.user.team.add(team)

        return HttpResponseRedirect("/%i" % team.id)

    else:
        form = CreateTeamForm()

    return render(response, "create.html", {"form": form})


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
                return HttpResponseRedirect("add_teams_to_league")

        else:
            return render(response, "join_to_league.html")
    else:
        form = JoinLeagueForm()
    return render(response, 'join_to_league.html', {"all_leagues": all_leagues, "form": form})


@login_required
def add_teams_to_league(response):

    if response.method == "POST":
        user_teams=response.user.team.all()
        user_team_names=[team.name for team in user_teams]
        form = AddTeamToLeague(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name in user_team_names:
                return HttpResponseRedirect("add_teams_to_league.html")
        else:
            return HttpResponseRedirect("add_team_to_league.html")
    else:
        print('cccc')
        form = AddTeamToLeague()
    return render(response, "add_team_to_league.html", {"form": form})


@login_required
def index(response, id):
    today = date.today().strftime('%Y%m%d')
    team = Team.objects.get(id=id)
    all_players = Player.objects.all()  # <Player: Player object (id)>

    if team in response.user.team.all() and today != '20200105':
        if response.method == "POST":
            print("response post")
            if response.POST.get("save"):
                for item in team:
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player1:
                        old_price = team.player1.price
                    if team.budget + old_price >= player.price:
                        team.player1 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                else:
                    print("invalid")

            elif response.POST.get("newItem2"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player2:
                        old_price = team.player2.price
                    if team.budget + old_price >= player.price:
                        team.player2 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                else:
                    print("invalid")

            elif response.POST.get("newItem3"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player3:
                        old_price = team.player3.price
                    if team.budget + old_price >= player.price:
                        team.player3 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                else:
                    print("invalid")

            elif response.POST.get("newItem4"):
                player_id = response.POST.get("chosenPlayer")
                if player_id:
                    player = Player.objects.filter(id=player_id)[0]
                    old_price = 0
                    if team.player4:
                        old_price = team.player4.price
                    if team.budget + old_price >= player.price:
                        team.player4 = player
                        team.budget = team.budget - player.price + old_price
                        team.save()
                else:
                    print("invalid")

        return render(response, "list.html", {"team": team, "all_players": all_players})

    return render(response, "home.html")


@login_required
def view(request):
    return render(request, "view.html")


@login_required
def leagues(response):
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
                return HttpResponseRedirect("add_teams_to_league" % league.id)
            else:
                return render(response, 'leagues.html', {"form": form})

    else:
        form = CreateLeagueForm()

    return render(response, "leagues.html", {"form": form})


@login_required
def chosen_league(response, id):
    return render(response, 'team_to_league.html')
