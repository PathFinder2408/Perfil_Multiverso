from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('certificacion/', views.PublicProyectoListView.as_view(), name='certificacion_obras'),
    path('', TemplateView.as_view(template_name='obras_index.html'), name='obras_index'),
    path('ingenieros/', views.IngenieroListView.as_view(), name='ingeniero_list'),
    path('ingenieros/nuevo/', views.IngenieroCreateView.as_view(), name='ingeniero_create'),
    path('ingenieros/<str:pk>/editar/', views.IngenieroUpdateView.as_view(), name='ingeniero_update'),
    path('ingenieros/<str:pk>/eliminar/', views.IngenieroDeleteView.as_view(), name='ingeniero_delete'),

    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<str:pk>/editar/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<str:pk>/eliminar/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),

    path('asignaciones/', views.AsignacionListView.as_view(), name='asignacion_list'),
    path('asignaciones/nueva/', views.AsignacionCreateView.as_view(), name='asignacion_create'),
    path('asignaciones/<int:pk>/editar/', views.AsignacionUpdateView.as_view(), name='asignacion_update'),
    path('asignaciones/<int:pk>/eliminar/', views.AsignacionDeleteView.as_view(), name='asignacion_delete'),
]
