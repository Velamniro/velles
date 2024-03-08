from django.urls import path

from . import views

urlpatterns = [
    path('favourite/add/<slug:slug>', views.favourite_add, name='favourite_add'),
]