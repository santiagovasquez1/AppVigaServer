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

# viga_detail=VigaView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# viga_myGet=VigaView.as_view({
#     'get':'myGet'
# },renderer_classes=[renderers.StaticHTMLRenderer])

# cortante_calc=cortanteVigaView.as_view({

# })

router = DefaultRouter()
router.register(r'vigas',VigaView)
urlpatterns=router.urls

urlpatterns += [
    path('admin/', admin.site.urls)
]
