from rest_framework import serializers
from ..models import Exemplaire

class ExemplaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplaire
        fields = ['id', 'état', 'date_acquisition', 'localisation', 'disponibilité']
