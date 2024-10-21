from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Auteur
from ..serializers import AuteurSerializer
from ..permission import Admin, Editor, Viewer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
