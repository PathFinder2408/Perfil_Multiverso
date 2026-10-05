from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_ti, name='inicio_ti'),
    path('stack/', views.stack_tecnologico, name='stack_ti'),

    path('proyecto/nuevo/', views.ProyectoDigitalCreateView.as_view(), name='ti_proyecto_create'),
    path('proyecto/<int:pk>/editar/', views.ProyectoDigitalUpdateView.as_view(), name='ti_proyecto_update'),
    path('proyecto/<int:pk>/eliminar/', views.ProyectoDigitalDeleteView.as_view(), name='ti_proyecto_delete'),

    path('certificacion/nueva/', views.CertificacionCreateView.as_view(), name='ti_certificacion_create'),
    path('certificacion/<int:pk>/editar/', views.CertificacionUpdateView.as_view(), name='ti_certificacion_update'),
    path('certificacion/<int:pk>/eliminar/', views.CertificacionDeleteView.as_view(), name='ti_certificacion_delete'),
]