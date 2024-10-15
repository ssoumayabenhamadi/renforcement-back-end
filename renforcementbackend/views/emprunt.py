from rest_framework import viewsets
from ..models import Emprunt
from ..serializers import EmpruntSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer