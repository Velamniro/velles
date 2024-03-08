from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from home_app.models import File

# Create your views here.
@login_required
def favourite_add(request, slug):
    file = get_object_or_404(File, slug=slug)
    if request.user.favourites.filter(pk=file.pk).exists():
        request.user.favourites.remove(file)
    else:
        request.user.favourites.add(file)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])