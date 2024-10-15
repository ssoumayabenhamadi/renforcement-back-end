from rest_framework import viewsets
from ..models import Editeur
from ..serializers import EditeurSerializer

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer