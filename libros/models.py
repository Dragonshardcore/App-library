from django.db import models

class Libro(models.Model):
    # Definimos los campos básicos del libro
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    # Usamos URLField para guardar el link de la imagen (de Google o Amazon)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    # Relacionamos la reserva con un libro específico
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    # Guardamos el nombre del usuario y las fechas
    usuario = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"Reserva de {self.libro.titulo} por {self.usuario}"