from .models import Coodenada
from rest_framework import viewsets
from .serializers import CoordenadaSerializer


class CoordenadaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coodenada.objects.all()
    serializer_class = CoordenadaSerializer