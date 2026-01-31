from django.contrib import admin
from .models import Autor, Libro, Reserva

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Reserva)
