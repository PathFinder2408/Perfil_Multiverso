"""
URL configuration for portafolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ti/', include('arquitectura_ti.urls')),
    path('obras/', include('obras_civiles.urls')),
    path('cuentas/', include('django.contrib.auth.urls')), # login, logout, etc
    path('', TemplateView.as_view(template_name='landing.html'), name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
