from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(),
         name='pokemon_detail'),

    path('move/<int:pk>/', views.MoveDetailView.as_view(),
         name='move_detail'),

    path('ability/<int:pk>/', views.AbilityDetailView.as_view(),
         name='ability_detail'),

    path('type/<int:pk>/', views.TypeDetailView.as_view(),
         name='type_detail'),

]
