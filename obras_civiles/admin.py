from django.contrib import admin
from .models import Ingeniero, Proyecto, Asignacion

@admin.register(Ingeniero)
class IngenieroAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'email')
    search_fields = ('rut', 'nombre', 'apellido')

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'presupuesto', 'activo')
    list_filter = ('activo',)
    search_fields = ('codigo', 'nombre')

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('ingeniero', 'proyecto', 'rol_en_proyecto', 'fecha_asignacion')
    list_filter = ('proyecto',)
