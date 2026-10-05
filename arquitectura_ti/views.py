import json
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from .models import ProyectoDigital, Certificacion, Tecnologia
from .forms import ProyectoDigitalForm, CertificacionForm

def inicio_ti(request):
    proyectos = ProyectoDigital.objects.all().order_by('-fecha_publicacion')
    certificaciones = Certificacion.objects.all().order_by('-fecha_obtencion')
    return render(request, 'ti_index.html', {
        'proyectos_db': proyectos,
        'certificaciones_db': certificaciones
    })

def stack_tecnologico(request):
    return render(request, 'ti_stack.html')

# --- CRUD PARA PROYECTOS DIGITALES (CON TRANSACCIÓN) ---

class ProyectoDigitalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProyectoDigital
    form_class = ProyectoDigitalForm
    template_name = 'ti_form.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.add_proyectodigital'

    def form_valid(self, form):
        with transaction.atomic():
            # 1. Guardar el proyecto (transacción inicia)
            self.object = form.save()
            # 2. Actualizar contador de experiencia en Tecnologias
            for tech in self.object.tecnologias.all():
                tech.usos_contador += 1
                tech.save()
        return super().form_valid(form)

class ProyectoDigitalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProyectoDigital
    form_class = ProyectoDigitalForm
    template_name = 'ti_form.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.change_proyectodigital'

    def form_valid(self, form):
        with transaction.atomic():
            # Restaurar contadores de las tecnologías viejas
            old_techs = ProyectoDigital.objects.get(pk=self.object.pk).tecnologias.all()
            for tech in old_techs:
                tech.usos_contador = max(0, tech.usos_contador - 1)
                tech.save()
            
            # Guardar nuevos cambios
            self.object = form.save()

            # Sumar a las nuevas tecnologías seleccionadas
            for tech in self.object.tecnologias.all():
                tech.usos_contador += 1
                tech.save()

        return super().form_valid(form)

class ProyectoDigitalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProyectoDigital
    template_name = 'ti_confirm_delete.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.delete_proyectodigital'

    def delete(self, request, *args, **kwargs):
        with transaction.atomic():
            self.object = self.get_object()
            for tech in self.object.tecnologias.all():
                tech.usos_contador = max(0, tech.usos_contador - 1)
                tech.save()
            return super().delete(request, *args, **kwargs)

# --- CRUD PARA CERTIFICACIONES ---

class CertificacionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Certificacion
    form_class = CertificacionForm
    template_name = 'ti_form.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.add_certificacion'

class CertificacionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Certificacion
    form_class = CertificacionForm
    template_name = 'ti_form.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.change_certificacion'

class CertificacionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Certificacion
    template_name = 'ti_confirm_delete.html'
    success_url = reverse_lazy('inicio_ti')
    permission_required = 'arquitectura_ti.delete_certificacion'