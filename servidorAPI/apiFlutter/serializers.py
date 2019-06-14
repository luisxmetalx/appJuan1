from .models import Coodenada 
from rest_framework import serializers


class CoordenadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coodenada
        fields = ('latitud', 'longitud')


