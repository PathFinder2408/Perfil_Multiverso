from django.db import models

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    icono_css = models.CharField(max_length=100, help_text="Ej: devicon-python-plain colored")
    usos_contador = models.IntegerField(default=0, help_text="Se actualiza automáticamente por transacción")

    def __str__(self):
        return f"{self.nombre} ({self.usos_contador} usos)"

class ProyectoDigital(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='proyectos', blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Certificacion(models.Model):
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    en_curso = models.BooleanField(default=False)
    fecha_obtencion = models.DateField(blank=True, null=True)
    credencial_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"
