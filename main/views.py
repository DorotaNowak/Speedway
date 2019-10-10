from django.shortcuts import render
from django.http import HttpResponse
def test_response(request):
    return HttpResponse('tu bedzie pierwsza strona z paskiem')
# Create your views here.
