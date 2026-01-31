from rest_framework import serializers
from .models import Autor, Libro, Reserva


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(
        source="autor.__str__", read_only=True
    )
    class Meta:
        model = Libro
        fields = '__all__'
        # autor se maneja por ID automáticamente (ForeignKey)


class ReservaSerializer(serializers.ModelSerializer):
    libro_nombre = serializers.CharField(
        source="libro.__str__", read_only=True
    )

    class Meta:
        model = Reserva
        fields = "__all__"
