import json
import os
from django.shortcuts import render
from django.conf import settings

def inicio_ti(request):
    ruta = os.path.join(settings.BASE_DIR, 'data', 'tech_data.json')
    with open(ruta, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return render(request, 'ti_index.html', {'datos': datos})

def stack_tecnologico(request):
    return render(request, 'ti_stack.html') # Segunda vista requerida