import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from obras_civiles.models import Ingeniero, Proyecto, Asignacion

def setup():
    # Modelos
    models = [Ingeniero, Proyecto, Asignacion]
    
    # Grupos
    admin_group, _ = Group.objects.get_or_create(name='Administrador')
    operador_group, _ = Group.objects.get_or_create(name='Operador')
    consulta_group, _ = Group.objects.get_or_create(name='Consulta')

    for model in models:
        content_type = ContentType.objects.get_for_model(model)
        
        # Permisos
        add_perm = Permission.objects.get(content_type=content_type, codename=f'add_{model._meta.model_name}')
        change_perm = Permission.objects.get(content_type=content_type, codename=f'change_{model._meta.model_name}')
        delete_perm = Permission.objects.get(content_type=content_type, codename=f'delete_{model._meta.model_name}')
        view_perm = Permission.objects.get(content_type=content_type, codename=f'view_{model._meta.model_name}')
        
        # Administrador (Todos)
        admin_group.permissions.add(add_perm, change_perm, delete_perm, view_perm)
        
        # Operador (Crear, Modificar, Consultar)
        operador_group.permissions.add(add_perm, change_perm, view_perm)
        
        # Consulta (Consultar)
        consulta_group.permissions.add(view_perm)

    print("Grupos y permisos creados exitosamente.")

    # Crear Usuarios de prueba
    users_data = [
        ('admin1', 'admin123', admin_group, True),
        ('operador1', 'operador123', operador_group, False),
        ('consulta1', 'consulta123', consulta_group, False)
    ]

    for username, password, group, is_staff in users_data:
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = is_staff  # Solo el admin real entra al django-admin o is_staff=True si es requerido
            if group == admin_group:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            user.groups.add(group)
            print(f"Usuario {username} creado.")
        else:
            print(f"Usuario {username} ya existe.")

if __name__ == '__main__':
    setup()

    # Nuevos permisos de Arquitectura TI
    ti_models = ['proyectodigital', 'certificacion']
    ti_perms = Permission.objects.filter(content_type__model__in=ti_models)
    admin_group.permissions.add(*ti_perms)
    operador_group.permissions.add(*ti_perms.filter(codename__startswith='add_') | ti_perms.filter(codename__startswith='change_'))
    print('Permisos TI actualizados.')
