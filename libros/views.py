from rest_framework import viewsets
from .models import Autor, Libro, Reserva
from .serializers import AutorSerializer, LibroSerializer, ReservaSerializer

# VIEWSET AUTOR
class AutorViewSet(viewsets.ModelViewSet):
     # Obtiene todos los autores
    queryset = Autor.objects.all()
     # Usa el serializer de Autor
    serializer_class = AutorSerializer

# VIEWSET LIBRO

class LibroViewSet(viewsets.ModelViewSet):
     # Obtiene todos los libros
    queryset = Libro.objects.all()
     # Usa el serializer de Libro
    serializer_class = LibroSerializer

# VIEWSET RESERVA
class ReservaViewSet(viewsets.ModelViewSet):
     # Obtiene todas las reservas
    queryset = Reserva.objects.all()
     # Usa el serializer de Reserva
    serializer_class = ReservaSerializer
