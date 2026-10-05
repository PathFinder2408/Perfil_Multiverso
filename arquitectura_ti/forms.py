from django import forms
from .models import ProyectoDigital, Certificacion, Tecnologia

class ProyectoDigitalForm(forms.ModelForm):
    tecnologias = forms.ModelMultipleChoiceField(
        queryset=Tecnologia.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = ProyectoDigital
        fields = ['nombre', 'descripcion', 'github_url', 'live_url', 'tecnologias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'live_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class CertificacionForm(forms.ModelForm):
    class Meta:
        model = Certificacion
        fields = ['titulo', 'institucion', 'en_curso', 'fecha_obtencion', 'credencial_url']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'en_curso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_obtencion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'credencial_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
