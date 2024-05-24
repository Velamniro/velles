from django.urls import path

from . import views

urlpatterns = [
    path('favourites/add/<slug:slug>', views.favourite_add, name='favour_add'),
    path('favourites/<slug:game_slug>/<slug:type_slug>/', views.FavouritesViewFiltered.as_view(), name='favour_filtered_with_type'),
    path('favourites/<slug:game_slug>/', views.FavouritesViewFiltered.as_view(), name='favour_filtered'),
    path('favourites/', views.FavouritesView.as_view(), name='favours'),
]