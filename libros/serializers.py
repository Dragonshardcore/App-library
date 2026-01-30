from rest_framework import serializers
from .models import Libro, Reserva

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__' # Significa: "Pasa todos los campos (id, titulo, autor)"

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'