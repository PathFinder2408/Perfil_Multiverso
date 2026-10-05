from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ingeniero, Proyecto, Asignacion
from .forms import IngenieroForm, ProyectoForm, AsignacionForm

# --- INGENIERO ---
class IngenieroListView(LoginRequiredMixin, ListView):
    model = Ingeniero
    template_name = 'obras_civiles/ingeniero_list.html'
    context_object_name = 'ingenieros'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q) | queryset.filter(rut__icontains=q)
        return queryset

class IngenieroCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Ingeniero
    form_class = IngenieroForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('ingeniero_list')
    permission_required = 'obras_civiles.add_ingeniero'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Ingeniero'
        return context

class IngenieroUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ingeniero
    form_class = IngenieroForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('ingeniero_list')
    permission_required = 'obras_civiles.change_ingeniero'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificar Ingeniero'
        return context

class IngenieroDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ingeniero
    template_name = 'obras_civiles/confirm_delete.html'
    success_url = reverse_lazy('ingeniero_list')
    permission_required = 'obras_civiles.delete_ingeniero'

# --- PROYECTO ---
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'obras_civiles/proyecto_list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q) | queryset.filter(codigo__icontains=q)
        return queryset

class ProyectoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'obras_civiles.add_proyecto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Proyecto'
        return context

class ProyectoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'obras_civiles.change_proyecto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificar Proyecto'
        return context

class ProyectoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'obras_civiles/confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'obras_civiles.delete_proyecto'

# --- ASIGNACION ---
class AsignacionListView(LoginRequiredMixin, ListView):
    model = Asignacion
    template_name = 'obras_civiles/asignacion_list.html'
    context_object_name = 'asignaciones'

class AsignacionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('asignacion_list')
    permission_required = 'obras_civiles.add_asignacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Asignación'
        return context

class AsignacionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'obras_civiles/form.html'
    success_url = reverse_lazy('asignacion_list')
    permission_required = 'obras_civiles.change_asignacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificar Asignación'
        return context

class AsignacionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Asignacion
    template_name = 'obras_civiles/confirm_delete.html'
    success_url = reverse_lazy('asignacion_list')
    permission_required = 'obras_civiles.delete_asignacion'