from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom
