from rest_framework import viewsets
from ..models import Livre
from ..serializers import LivreSerializer
from ..filtres.livre_pagination import LivrePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    pagination_class = LivrePagination
    permission_classes = [IsAuthenticated]  


    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filterset_fields = ['auteurs__nom', 'categories__nom']
    ordering_fields = ['titre', 'date_de_publication']
    ordering = ['titre']