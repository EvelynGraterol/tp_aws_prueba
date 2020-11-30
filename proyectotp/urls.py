"""proyectotp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import proyectotpapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('azar_decimal', proyectotpapp.views.numero_al_azar_decimal),
    path('azar_entero/<int:param1>/<int:param2>', proyectotpapp.views.numero_al_azar_entero_en_rango),     
]
