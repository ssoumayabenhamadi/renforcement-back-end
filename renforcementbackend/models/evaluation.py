from django.db import models

class Evaluation(models.Model):
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commentaire = models.TextField(null=True, blank=True)
    date_évaluation = models.DateTimeField(auto_now_add=True)
    recommandé = models.BooleanField(default=False)
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.note
