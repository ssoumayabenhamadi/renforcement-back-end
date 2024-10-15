from rest_framework import serializers
from ..models import Editeur

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = ['id', 'nom', 'adresse', 'site_web', 'email_contact', 'description', 'logo']
