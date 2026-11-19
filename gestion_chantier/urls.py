from django.urls import path
from gestion_chantier import views


urlpatterns = [
     path('', views.dashboard, name='dashboard'),

    # PROJETS
    path('projets/', views.liste_projets, name='liste_projets'),
    path('projets/ajouter/', views.ajouter_projet, name='ajouter_projet'),
    path('projets/modifier/<int:id>/', views.modifier_projet, name='modifier_projet'),
    path('projets/supprimer/<int:id>/', views.supprimer_projet, name='supprimer_projet'),

    # MAITRES
    path('maitres/', views.liste_maitre_ouvrage, name='liste_maitre_ouvrage'),
    path('maitres/ajouter/', views.ajouter_maitre_ouvrage, name='ajouter_maitre_ouvrage'),
    path('maitres/modifier/<int:pk>/', views.modifier_maitre_ouvrage, name='modifier_maitre_ouvrage'),
    path('maitres/supprimer/<int:pk>/', views.supprimer_maitre_ouvrage, name='supprimer_maitre_ouvrage'),
]