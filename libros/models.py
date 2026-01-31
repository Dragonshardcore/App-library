from django.db import models

class Autor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Libro(models.Model):
   titulo = models.CharField(max_length=200)
   autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
   genero = models.CharField(max_length=50, blank=True, null=True)
   anio_publicacion = models.PositiveIntegerField(blank=True, null=True)
   descripcion = models.TextField(blank=True, null=True)
   imagen_url = models.URLField(max_length=500, blank=True, null=True)
   
   def __str__(self):
       return self.titulo


class Reserva(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"Reserva de {self.libro.titulo} por {self.usuario}"
