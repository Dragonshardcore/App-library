from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, ReservaViewSet, AutorViewSet

# Router de DRF
router = DefaultRouter()

# Registro de rutas automáticas
router.register(r'libros', LibroViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'autores', AutorViewSet)

# URLs finales de la API
urlpatterns = [
    path('', include(router.urls)),
]
