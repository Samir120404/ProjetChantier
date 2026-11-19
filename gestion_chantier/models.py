from django.db import models


# =========================
# MAITRE D'OUVRAGE
# =========================
class MaitreOuvrage(models.Model):
    TYPE_CHOICES = [
        ('Particulier', 'Particulier'),
        ('Entreprise', 'Entreprise'),
        ('Etat', 'Etat'),
    ]

    nom = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.nom


# =========================
# PROJET CHANTIER
# =========================
class ProjetChantier(models.Model):
    TYPE_PROJET = [
        ('Maison', 'Maison'),
        ('Immeuble', 'Immeuble'),
        ('Route', 'Route'),
        ('Pont', 'Pont'),
        ('Autre', 'Autre'),
    ]

    STATUT = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Suspendu', 'Suspendu'),
        ('Terminé', 'Terminé'),
    ]

    maitre_ouvrage = models.ForeignKey(
        MaitreOuvrage,
        on_delete=models.CASCADE,
        related_name='projets'
    )

    nom_projet = models.CharField(max_length=200)
    code_projet = models.CharField(max_length=50, unique=True)
    type_projet = models.CharField(max_length=30, choices=TYPE_PROJET)

    description = models.TextField()
    adresse_chantier = models.CharField(max_length=255)
    coordonnees_gps = models.CharField(max_length=100, blank=True, null=True)

    date_debut = models.DateField()
    date_fin_prevue = models.DateField()
    duree_projet = models.PositiveIntegerField(help_text="Durée en jours")

    budget_previsionnel = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT,
        default='En attente'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_projet