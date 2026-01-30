from rest_framework import viewsets
from .models import Libro, Reserva
from .serializers import LibroSerializer, ReservaSerializer

# El ViewSet maneja automáticamente GET, POST, PUT y DELETE
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # Los permisos se heredan del settings.py (Lectura pública / Escritura privada)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer