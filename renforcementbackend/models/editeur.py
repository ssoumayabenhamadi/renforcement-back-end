from django.db import models

class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    site_web = models.URLField(null=True, blank=True)
    email_contact = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logos_editeurs/', null=True, blank=True)

    def __str__(self):
        return self.nom
