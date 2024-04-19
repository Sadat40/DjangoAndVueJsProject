from django.urls import path

from . import views

app_name = "movies"


urlpatterns = [
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
    path("characters/<int:pk>", views.CharacterDetailView.as_view(), name="character_detail"),
    path("characters/new", views.CharacterCreateView.as_view(), name="character_create"),
    path("characters/update/<int:pk>", views.CharacterUpdateView.as_view(),
         name="character_update"),
    path("characters/delete/<int:pk>", views.CharacterDeleteView.as_view(),
         name="character_delete"),
    path("games/", views.GameListView.as_view(), name="game_list"),
    path("games/new", views.GameCreateView.as_view(), name="Game_create"),
    path("games/<int:pk>", views.GameDetailView.as_view(),
         name="game_detail"),
    path("games/update/<int:pk>", views.GameUpdateView.as_view(),
         name="game_update"),
    path("games/delete/<int:pk>", views.GameDeleteView.as_view(),
         name="game_delete"),
    path("games/update_bis/<int:pk>", views.GameUpdatebisView.as_view(), name="game_update_bis",),
     path(
"games/update_bis/<int:pk>",
views.GameUpdatebisView.as_view(),
name="game_update_bis",
),
     path(
"games/bis/<int:pk>",
views.GameDetailbisView.as_view(),
name="game_detail_bis",
),
     
     path(
"games/js/<int:pk>",
views.GameDetailJsView.as_view(),
name="game_detail_js",
),
]
