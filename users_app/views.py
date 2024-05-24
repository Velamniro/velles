"""Copyright 2024 Velamniro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Any

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from home_app.models import File, Type, Game

# Create your views here.
@login_required
def favourite_add(request, slug):
    file = get_object_or_404(File, slug=slug)
    if request.user.favourites.filter(pk=file.pk).exists():
        request.user.favourites.remove(file)
    else:
        request.user.favourites.add(file)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class FavouritesView(ListView):
    model = File
    template_name = 'share/home-favours.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Избранное — Velles"
        context['types'] = Type.objects.all()
        context['games'] = Game.objects.all()
        context['mode'] = 'favours'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return File.objects.filter(favourite=self.request.user)

class FavouritesViewFiltered(FavouritesView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['game_slug'] = self.kwargs['game_slug']
        try:
            context['type_slug'] = self.kwargs['type_slug']
        finally:
            return context
    
    def get_queryset(self) -> QuerySet[Any]:
        game = Game.objects.get(slug=self.kwargs['game_slug'])
        try:
            type = Type.objects.get(slug=self.kwargs['type_slug'])
            return File.objects.filter(game=game, type=type).order_by('-create_datetime')
        except KeyError:
            return File.objects.filter(game=game).order_by('-create_datetime')