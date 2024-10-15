from rest_framework import viewsets
from ..models import Exemplaire
from ..serializers import ExemplaireSerializer

class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer