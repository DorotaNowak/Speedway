from .models import Team, Player
from .forms import CreateTeamForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def test_response(request):
    return HttpResponse('tu bedzie pierwsza strona z paskiem')


def home_response(request):
    return render(request, 'login.html')


@login_required(redirect_field_name='')
def after_login_response(request):
    return render(request, 'home.html')


def home(response):
    return render(response, "home.html", {})


@login_required(redirect_field_name='')
def create(response):
    if response.method == "POST":
        form = CreateTeamForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Team(name=n, budget=10.0, player1=None, player2=None, player3=None, player4=None)
            t.save()  # save to database
            response.user.team.add(t)

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateTeamForm()

    return render(response, "create.html", {"form": form})


@login_required(redirect_field_name='')
def index(response, id):
    team = Team.objects.get(id=id)
    players = Player.objects.all()  # <Player: Player object (id)>

    if team in response.user.team.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in team.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    pl = Player.objects.filter(first_name=txt)[0]
                    team.player1 = pl
                    team.save()
                    print(team)
                    print(pl)
                else:
                    print("invalid")

        return render(response, "list.html", {"ls": team, "query_results": players})

    return render(response, "home.html", {})


@login_required
def view(request):
    l = Team.objects.all()
    return render(request, "view.html", {"lists": l})


@login_required
def view(response):
    return render(response, "view.html", {})
