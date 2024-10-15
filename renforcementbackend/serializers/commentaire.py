from rest_framework import serializers
from ..models import Commentaire

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'contenu', 'date_publication', 'note', 'visible', 'modéré']
