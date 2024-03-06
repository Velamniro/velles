from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {'title': "Главная -- Velles"}
    return render(request, 'home_app/index.html', data)

def about(request):
    data = {'title': "Все про сайт -- Velles"}
    return render(request, 'home_app/about.html', data)