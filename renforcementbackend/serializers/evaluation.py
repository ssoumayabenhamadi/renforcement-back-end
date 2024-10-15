from rest_framework import serializers
from ..models import Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['id', 'note', 'commentaire', 'date_évaluation', 'recommandé', 'titre']
