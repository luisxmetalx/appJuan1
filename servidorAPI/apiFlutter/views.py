from .models import Coodenada
from rest_framework import viewsets, status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CoordenadaSerializer


@api_view(['GET', 'POST'])
def coordenada_list(request, format=None):
    """
    List all code snippets, or create a new Coordenadas.
    """
    if request.method == 'GET':
        coordenadas = Coodenada.objects.all()
        serializer = CoordenadaSerializer(coordenadas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoordenadaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def coordenada_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code Coordenadas.
    """
    try:
        coordenada = Coodenada.objects.get(pk=pk)
    except coordenada.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoordenadaSerializer(coordenada)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoordenadaSerializer(coordenada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coordenada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CoordenadaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coodenada.objects.all()
    serializer_class = CoordenadaSerializer