from rest_framework import serializers
from ..models import Livre

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['id', 'titre', 'résumé', 'date_de_publication', 'isbn', 'nombre_de_pages', 'langue', 'image_de_couverture', 'editeur', 'format']
