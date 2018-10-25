"""Tec_Web_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core.views import *

urlpatterns = [
	path('', index),
	path('index', index),
	path('lista_de_cursos', lista_de_cursos),
	path('adm', adm),
	path('ads', ads),
	path('adsead', adsead),
	path('bancodedados', bancodedados),
	path('detalhe_de_curso', detalhe_de_curso),
	path('eng_comput', eng_comput),
	path('gestao_ti', gestao_ti),
	path('jogos_digitais', jogos_digitais),
	path('noticias', noticias),
	path('processos_gerenciais', processos_gerenciais),
	path('producao_multimedia', producao_multimedia),
	path('redes_computadores', redes_computadores),
	path('si', si),
    path('admin', admin.site.urls),
]
