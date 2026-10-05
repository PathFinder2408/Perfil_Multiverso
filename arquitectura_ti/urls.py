from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_ti, name='inicio_ti'),
    path('stack/', views.stack_tecnologico, name='stack_ti'),
]