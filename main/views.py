from django.shortcuts import render
from django.http import HttpResponse




def test_response(request):
    return HttpResponse('tu bedzie pierwsza strona z paskiem')
# Create your views here.
def home_response(request):
    return render(request, 'home.html')
def after_login_response(request):
    return render(request,'after_login.html')
def league_page(request):
    return render(request, 'leagues.html')
def stats_page(request):
    return render(request,'stats.html')
def ranking_page(request):
    return render(request,'ranking.html')