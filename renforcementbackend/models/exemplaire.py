from django.db import models

class Exemplaire(models.Model):
    état = models.CharField(max_length=50)
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=100)
    disponibilité = models.BooleanField(default=True)

    def __str__(self):
        return f"self.localisation"
