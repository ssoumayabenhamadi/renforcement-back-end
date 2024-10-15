from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_de_naissance = models.DateField()
    date_de_décès = models.DateField(null=True, blank=True)
    nationalité = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_auteurs/', null=True, blank=True)

    def __str__(self):
        return self.nom
