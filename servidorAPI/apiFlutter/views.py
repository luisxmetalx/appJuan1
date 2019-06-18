from .models import RegistroGpsMovil
from rest_framework import viewsets, status, permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistroGpsMovilSerializer


@api_view(['GET', 'POST'])
def coordenada_list(request, format=None):
    """
    List all code snippets, or create a new Coordenadas.
    """
    
    if request.method == 'GET':
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
        coordenadas = RegistroGpsMovil.objects.all()
        serializer = RegistroGpsMovilSerializer(coordenadas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
        serializer = RegistroGpsMovilSerializer(data=request.data)
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
        coordenada = RegistroGpsMovil.objects.get(pk=pk)
    except coordenada.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
        serializer = RegistroGpsMovilSerializer(coordenada)
        return Response(serializer.data)

    elif request.method == 'PUT':
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
        serializer = RegistroGpsMovilSerializer(coordenada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
        coordenada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegistroGpsMovilViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = RegistroGpsMovil.objects.all()
    serializer_class = RegistroGpsMovilSerializer
