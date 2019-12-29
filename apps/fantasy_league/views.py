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
            team = Team(name=name, budget=10.0, player1=None, player2=None, player3=None, player4=None)
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
                txt = response.POST.get("choosenPlayer")
                if txt:
                    player = Player.objects.filter(first_name=txt)[0]
                    team.player1 = player
                    team.save()
                else:
                    print("invalid")

        return render(response, "list.html", {"team": team, "all_players": all_players})

    return render(response, "home.html")


@login_required
def view(request):
    return render(request, "view.html")
