from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'ingenieros', api_views.IngenieroViewSet, basename='api-ingenieros')
router.register(r'proyectos', api_views.ProyectoViewSet, basename='api-proyectos')
router.register(r'asignaciones', api_views.AsignacionViewSet, basename='api-asignaciones')

urlpatterns = [
    path('', include(router.urls)),
]
