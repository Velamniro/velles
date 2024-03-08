from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import File

# Create your views here.
class HomeView(ListView):
    # data = {'title': "Главная -- Velles"}
    # return render(request, 'home_app/.html', data)
    model = File
    template_name = "home_app/index.html"
    extra_context = {
        'title': "Главная -- Velles"
    }
    context_object_name = 'files'

def about(request):
    data = {'title': "Все про сайт -- Velles"}
    return render(request, 'home_app/about.html', data)