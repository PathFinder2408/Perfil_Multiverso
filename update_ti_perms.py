import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

def update_perms():
    admin_group = Group.objects.get(name='Administrador')
    operador_group = Group.objects.get(name='Operador')

    ti_models = ['proyectodigital', 'certificacion']
    ti_perms = Permission.objects.filter(content_type__model__in=ti_models)
    
    admin_group.permissions.add(*ti_perms)
    
    # Operador no puede eliminar
    operador_perms = ti_perms.filter(codename__startswith='add_') | ti_perms.filter(codename__startswith='change_')
    operador_group.permissions.add(*operador_perms)
    
    print('Permisos de Arquitectura TI actualizados.')

if __name__ == '__main__':
    update_perms()
