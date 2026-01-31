from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, ReservaViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'autores', AutorViewSet)
urlpatterns = [
    path('', include(router.urls)),
]