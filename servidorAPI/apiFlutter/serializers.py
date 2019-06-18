from .models import RegistroGpsMovil 
from rest_framework import serializers


class RegistroGpsMovilSerializer(serializers.HyperlinkedModelSerializer):
    #coordenadas = serializers.PrimaryKeyRelatedField(many=True, queryset=RegistroGpsMovil.objects.all())

    class Meta:
        model = RegistroGpsMovil
        fields = (
            'latitud', 
            'longitud',
            'accuray',
            'altitude',
            'speed',
            'speed_accuracy',
            'marca_phone',
            'sist_operativo',
            'version',
            'imei',
            'mac_adress',
            'ip_adress',
            )


