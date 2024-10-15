from rest_framework import serializers
from ..models import Emprunt

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = ['id', 'date_emprunt', 'date_retour_prévue', 'date_retour_effective', 'statut', 'remarques']
