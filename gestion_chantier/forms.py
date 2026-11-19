from django import forms
from .models import ProjetChantier, MaitreOuvrage


class ProjetChantierForm(forms.ModelForm):

    class Meta:
        model = ProjetChantier
        fields = '__all__'

        widgets = {
            'maitre_ouvrage': forms.Select(attrs={'class': 'form-select'}),

            'nom_projet': forms.TextInput(attrs={'class': 'form-control'}),
            'code_projet': forms.TextInput(attrs={'class': 'form-control'}),
            'type_projet': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'adresse_chantier': forms.TextInput(attrs={'class': 'form-control'}),
            'coordonnees_gps': forms.TextInput(attrs={'class': 'form-control'}),

            'date_debut': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'date_fin_prevue': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'duree_projet': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_previsionnel': forms.NumberInput(attrs={'class': 'form-control'}),

            'statut': forms.Select(attrs={'class': 'form-select'}),
        }


class MaitreOuvrageForm(forms.ModelForm):

    class Meta:
        model = MaitreOuvrage
        fields = ['nom', 'contact', 'email', 'adresse']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
        }