from django.shortcuts import render
from gestion_chantier.models import ProjetChantier, MaitreOuvrage



def dashboard(request):
    return render(request, 'chantier/dashboard.html')