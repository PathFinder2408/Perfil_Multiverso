import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from arquitectura_ti.models import Tecnologia, ProyectoDigital, Certificacion

def populate():
    # 1. Crear Tecnologías
    techs = {
        'Python': 'devicon-python-plain',
        'Django': 'devicon-django-plain',
        'JavaScript': 'devicon-javascript-plain',
        'React': 'devicon-react-original',
        'MySQL': 'devicon-mysql-plain',
        'AWS EC2': 'devicon-amazonwebservices-original'
    }
    
    tech_objs = {}
    for nombre, icono in techs.items():
        obj, _ = Tecnologia.objects.get_or_create(nombre=nombre, defaults={'icono_css': icono})
        tech_objs[nombre] = obj

    # 2. Crear Certificaciones
    Certificacion.objects.get_or_create(
        titulo="Ingeniería en Informática",
        institucion="INACAP",
        defaults={'en_curso': True}
    )
    
    Certificacion.objects.get_or_create(
        titulo="Bootcamp Full Stack JavaScript Trainee V2.0",
        institucion="SENCE & Talento Digital / OTEC Posiciona",
        defaults={'en_curso': False, 'fecha_obtencion': date(2026, 9, 10)}
    )

    # 3. Crear Proyectos Digitales (y asignar tecnologías manualmente para iniciar los contadores)
    p1, created1 = ProyectoDigital.objects.get_or_create(
        nombre="Backend Perfil Multiverso",
        defaults={
            'descripcion': "API RESTful y plataforma administrativa construida para unificar portafolios profesionales. Incluye autenticación por JWT, vistas basadas en clases y arquitectura AWS.",
            'github_url': "https://github.com/PathFinder2408/Perfil_Multiverso"
        }
    )
    if created1:
        p1.tecnologias.add(tech_objs['Python'], tech_objs['Django'], tech_objs['MySQL'], tech_objs['AWS EC2'])
        for t in [tech_objs['Python'], tech_objs['Django'], tech_objs['MySQL'], tech_objs['AWS EC2']]:
            t.usos_contador += 1
            t.save()

    p2, created2 = ProyectoDigital.objects.get_or_create(
        nombre="Edific.life",
        defaults={
            'descripcion': "Plataforma web funcional que conecta a expertos del rubro con usuarios que buscan realizar obras. Gestión integral de proyectos constructivos en la nube.",
        }
    )
    if created2:
        p2.tecnologias.add(tech_objs['JavaScript'], tech_objs['React'], tech_objs['AWS EC2'])
        for t in [tech_objs['JavaScript'], tech_objs['React'], tech_objs['AWS EC2']]:
            t.usos_contador += 1
            t.save()

    p3, created3 = ProyectoDigital.objects.get_or_create(
        nombre="Algoritmos de Trading",
        defaults={
            'descripcion': "Desarrollo y backtesting de estrategias automatizadas para mercados financieros aplicando análisis de datos y matemáticas en Python.",
        }
    )
    if created3:
        p3.tecnologias.add(tech_objs['Python'])
        tech_objs['Python'].usos_contador += 1
        tech_objs['Python'].save()

    print("Datos de TI poblados exitosamente.")

if __name__ == '__main__':
    populate()
