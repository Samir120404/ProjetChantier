from django.shortcuts import render, redirect, get_object_or_404
from .models import ProjetChantier
from .forms import ProjetChantierForm
from .models import MaitreOuvrage
from django.shortcuts import render
from .forms import MaitreOuvrageForm, ProjetChantierForm


# LISTE
def liste_projets(request):
    projets = ProjetChantier.objects.all()
    return render(request, 'gestion_chantier/liste_projets.html', {'projets': projets})


# AJOUT
def ajouter_projet(request):
    form = ProjetChantierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_projets')

    return render(request, 'gestion_chantier/form_projet.html', {'form': form})


# MODIFIER
def modifier_projet(request, id):
    projet = get_object_or_404(ProjetChantier, id=id)
    form = ProjetChantierForm(request.POST or None, instance=projet)

    if form.is_valid():
        form.save()
        return redirect('liste_projets')

    return render(request, 'gestion_chantier/form_projet.html', {'form': form})


# SUPPRIMER
def supprimer_projet(request, id):
    projet = get_object_or_404(ProjetChantier, id=id)

    if request.method == 'POST':
        projet.delete()
        return redirect('liste_projets')

    return render(request, 'gestion_chantier/confirmer_suppression.html', {'projet': projet})




def dashboard(request):
    return render(request, 'chantier/base.html')






# LISTE
def liste_maitre_ouvrage(request):
    maitres = MaitreOuvrage.objects.all()
    return render(request, 'gestion_chantier/maitres/liste_maitre_ouvrage.html', {
    'maitres': maitres
})


# AJOUT
def ajouter_maitre_ouvrage(request):
    form = MaitreOuvrageForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('liste_maitre_ouvrage')

    return render(request, 'gestion_chantier/maitres/form_maitre_ouvrage.html', {
        'form': form
    })


# MODIFIER
def modifier_maitre_ouvrage(request, pk):
    maitre = get_object_or_404(MaitreOuvrage, pk=pk)
    form = MaitreOuvrageForm(request.POST or None, instance=maitre)
    if form.is_valid():
        form.save()
        return redirect('liste_maitre_ouvrage')
    return render(request, 'chantier/maitre/form_maitre_chantier.html', {'form': form})


# SUPPRIMER
def supprimer_maitre_ouvrage(request, pk):
    maitre = get_object_or_404(MaitreOuvrage, pk=pk)
    maitre.delete()
    return redirect('liste_maitre_ouvrage')


from django.shortcuts import render
import json
from .models import ProjetChantier, MaitreOuvrage

def dashboard(request):
    context = {
        'total_projets': ProjetChantier.objects.count(),
        'en_attente': ProjetChantier.objects.filter(statut='En attente').count(),
        'en_cours': ProjetChantier.objects.filter(statut='En cours').count(),
        'termines': ProjetChantier.objects.filter(statut='Terminé').count(),
        'total_maitres': MaitreOuvrage.objects.count(),
        'derniers_projets': ProjetChantier.objects.order_by('-date_creation')[:5],

        # DATA CHART
        'chart_labels': json.dumps(['En attente', 'En cours', 'Terminés']),
        'chart_data': json.dumps([
            ProjetChantier.objects.filter(statut='En attente').count(),
            ProjetChantier.objects.filter(statut='En cours').count(),
            ProjetChantier.objects.filter(statut='Terminé').count(),
        ])
    }

    return render(request, 'chantier/dashboard.html', context)