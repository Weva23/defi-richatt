from djongo import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

# Modèle des rôles (Admin, Contributeur, etc.)
class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

# Modèle des utilisateurs (hérité d'AbstractUser pour une gestion avancée)from django.contrib.auth.models import AbstractUser, Group, Permission
from djongo import models

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('contributeur', 'Contributeur')])
    points = models.IntegerField(default=0)

    groups = models.ManyToManyField(Group, related_name="utilisateur_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="utilisateur_permissions", blank=True)

    def __str__(self):
        return self.username


# Modèle des mots du dictionnaire
class Mot(models.Model):
    terme = models.CharField(max_length=255, unique=True)
    statut = models.CharField(
        max_length=50,
        choices=[('en attente', 'En attente'), ('valide', 'Validé')],
        default='en attente'
    )
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.terme

# Modèle des définitions des mots
class Definition(models.Model):
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name="definitions")
    texte = models.TextField()

    def __str__(self):
        return f"Définition de {self.mot.terme}"

# Modèle des variantes linguistiques des mots
class Variante(models.Model):
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name="variantes")
    forme_dérivée = models.CharField(max_length=255)
    type = models.CharField(max_length=50)  # Ex: singulier, pluriel, conjugaison...

    def __str__(self):
        return f"{self.forme_dérivée} ({self.type})"

# Modèle des validations de mots (Modération)
class Validation(models.Model):
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name="validations")
    validateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    statut = models.CharField(
        max_length=50,
        choices=[('accepté', 'Accepté'), ('rejeté', 'Rejeté')],
        default='en attente'
    )
    commentaire = models.TextField(null=True, blank=True)
    date_validation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Validation de {self.mot.terme} par {self.validateur.username}"

# Modèle des contributions des utilisateurs
class Contribution(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # Ex: "Ajout", "Modification"
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} a contribué à {self.mot.terme}"

# Modèle des commentaires sur un mot
class Commentaire(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name="commentaires")
    texte = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.utilisateur.username} sur {self.mot.terme}"

# Modèle des récompenses pour la gamification
class Recompense(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="recompenses")
    badge = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.badge}"

# Modèle des sources (Documents de référence)
class Source(models.Model):
    nom = models.CharField(max_length=255)
    lien = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

# Modèle pour l'importation de textes (Scraping, PDF, OCR...)
class ImportationTexte(models.Model):
    fichier_nom = models.CharField(max_length=255)
    mot_extrait = models.CharField(max_length=255)
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name="importations")
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_import = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Importation depuis {self.fichier_nom}"

# Modèle du challenge des 1000 mots (gamification)
class Challenge1000Mots(models.Model):
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)

    def __str__(self):
        return f"Challenge 1000 mots: {self.mot.terme}"

# Modèle pour relier les mots et leurs sources
class MotSource(models.Model):
    mot = models.ForeignKey(Mot, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mot.terme} - {self.source.nom}"
