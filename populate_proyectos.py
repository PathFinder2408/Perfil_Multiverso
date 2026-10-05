import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from obras_civiles.models import Proyecto

def populate():
    proyectos_data = [
        {
            "codigo": "PRJ-001",
            "nombre": "Instalación sanitaria en Totoralillo",
            "descripcion": "Ejecución de trabajos de gasfitería, excavación e instalación de tuberías sanitarias.",
            "presupuesto": 1500000.00,
            "fecha_inicio": date(2026, 5, 1)
        },
        {
            "codigo": "PRJ-002",
            "nombre": "Galpón para sede vecinal",
            "descripcion": "Diseño de la propuesta estructural y elaboración del presupuesto para una estructura de 8x10 metros.",
            "presupuesto": 8500000.00,
            "fecha_inicio": date(2026, 5, 15)
        },
        {
            "codigo": "PRJ-003",
            "nombre": "Autoconstrucción y mejoramiento",
            "descripcion": "Trabajos prácticos de construcción y cálculo de materiales utilizando estructuras Metalcon, placas OSB, paneles de cubierta PV4, redes de plomería y perfilería para iluminación LED COB de bajo voltaje.",
            "presupuesto": 3200000.00,
            "fecha_inicio": date(2026, 1, 10)
        },
        {
            "codigo": "PRJ-004",
            "nombre": "Plataforma Edific",
            "descripcion": "Desarrollo de la iniciativa web (ganadora de fondos CORFO) diseñada para conectar a expertos de la construcción con clientes.",
            "presupuesto": 15000000.00,
            "fecha_inicio": date(2026, 4, 1)
        },
        {
            "codigo": "PRJ-005",
            "nombre": "Proyecto Ayllu H2",
            "descripcion": "Evaluación de factibilidad y dimensionamiento técnico para el concepto de una planta de producción de hidrógeno verde alimentada por energía geotérmica en Cerro Pabellón.",
            "presupuesto": 25000000.00,
            "fecha_inicio": date(2026, 6, 1)
        }
    ]

    for data in proyectos_data:
        Proyecto.objects.update_or_create(
            codigo=data['codigo'],
            defaults={
                'nombre': data['nombre'],
                'descripcion': data['descripcion'],
                'presupuesto': data['presupuesto'],
                'fecha_inicio': data['fecha_inicio'],
                'activo': True
            }
        )
    print("Proyectos poblados correctamente.")

if __name__ == '__main__':
    populate()
