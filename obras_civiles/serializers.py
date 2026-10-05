from rest_framework import serializers
from .models import Ingeniero, Proyecto, Asignacion

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'

class IngenieroAdminSerializer(serializers.ModelSerializer):
    """
    Serializer para administradores: muestra toda la información,
    incluyendo campos sensibles (email, telefono, sueldo_base).
    """
    class Meta:
        model = Ingeniero
        fields = '__all__'

class IngenieroPublicSerializer(serializers.ModelSerializer):
    """
    Serializer para usuarios normales (Perfil Consulta/Operador):
    Oculta los campos sensibles exigidos por la rúbrica.
    """
    class Meta:
        model = Ingeniero
        # Excluimos explícitamente la información sensible (email, teléfono, sueldo)
        exclude = ('email', 'telefono', 'sueldo_base')
