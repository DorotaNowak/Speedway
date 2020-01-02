from .models import Team, Player
from .forms import CreateTeamForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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
def index(response, id):
    team = Team.objects.get(id=id)
    all_players = Player.objects.all()  # <Player: Player object (id)>

    if team in response.user.team.all():
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
