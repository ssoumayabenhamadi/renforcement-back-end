from rest_framework import serializers
from ..models import Auteur

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'biographie', 'date_de_naissance', 'date_de_décès', 'nationalité', 'photo']
