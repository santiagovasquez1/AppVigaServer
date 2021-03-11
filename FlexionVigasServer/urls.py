"""FlexionVigasServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from flexionVigas_api.views import VigaView
from flexionVigas_api.cortanteVigasModule.cortanteVigaView import cortanteVigaView

router = DefaultRouter()
router.register(r'vigas', VigaView)
urlpatterns = router.urls

cortante_disenio = cortanteVigaView.as_view({'post': 'post'})
cortante_chequeo = cortanteVigaView.as_view({'post': 'chequeoSeccion'})

urlpatterns += [
    path('admin/', admin.site.urls),
    path('cortante/disenio/', cortante_disenio, name='cortante_disenio'),
    path('cortante/chequeo/', cortante_chequeo, name='cortante_chequeo')
]
