from django.db import models

class Ingeniero(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, help_text="Ej: 12.345.678-9")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2, help_text="Dato sensible")
    foto = models.ImageField(upload_to='ingenieros/', blank=True, null=True)
    fecha_contratacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"

class Proyecto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"

class Asignacion(models.Model):
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE, related_name='asignaciones')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='asignaciones')
    rol_en_proyecto = models.CharField(max_length=100)
    fecha_asignacion = models.DateField(auto_now_add=True)
    documento_contrato = models.FileField(upload_to='contratos/', blank=True, null=True)

    class Meta:
        unique_together = ('ingeniero', 'proyecto')

    def __str__(self):
        return f"Asignación de {self.ingeniero} a {self.proyecto}"
