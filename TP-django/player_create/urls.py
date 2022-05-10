from django.urls import path
from . import views

urlpatterns = [
    path('player/formulaire/', views.formulaire_player),
    path('player/traitement/', views.traitement_player),
    path('player/', views.index_player), 
    path('player/affiche/<int:id>/', views.affiche_player),
    path('player/update/<int:id>/', views.update_player),
    path('player/updatetraitement/<int:id>/', views.updatetraitement_player),
    path('player/delete/<int:id>/', views.delete_player),

    path('team/formulaire/', views.formulaire_team),
    path('team/traitement/', views.traitement_team),
    path('team/', views.index_team),
    path('team/affiche/<int:id>/', views.affiche_team),
    path('team/update/<int:id>/', views.update_team),
    path('team/updatetraitement/<int:id>/', views.updatetraitement_team),
    path('team/delete/<int:id>/', views.delete_team),
]