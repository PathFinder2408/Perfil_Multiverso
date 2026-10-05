from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ingeniero, Proyecto, Asignacion
from .serializers import (
    IngenieroAdminSerializer, 
    IngenieroPublicSerializer,
    ProyectoSerializer, 
    AsignacionSerializer
)

class IngenieroViewSet(viewsets.ModelViewSet):
    queryset = Ingeniero.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # Si el usuario es administrador (o pertenece al grupo Administrador),
        # puede ver toda la información sensible.
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrador').exists():
            return IngenieroAdminSerializer
        # De lo contrario, retorna el serializer que oculta campos sensibles
        return IngenieroPublicSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    permission_classes = [IsAuthenticated]
