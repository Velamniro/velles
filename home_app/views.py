from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import File

# Create your views here.
class HomeView(ListView):
    model = File
    template_name = 'home_app/index.html'
    context_object_name = 'files'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная — Velles"
        return context

class FileView(DetailView):
    model = File
    template_name = 'home_app/fileview.html'
    context_object_name = 'file'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title} — Velles"
        return context

def about(request) -> HttpResponse:
    data = {'title': "Все про сайт -- Velles"}
    return render(request, 'home_app/about.html', data)