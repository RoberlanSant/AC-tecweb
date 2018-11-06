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
	path('disciplinas', disciplinas),
	path('disciplinas_adm', disciplinas_adm),
	path('disciplinas_ads', disciplinas_ads),
	path('disciplinas_ads_ead', disciplinas_ads_ead),
	path('disciplinas_ec', disciplinas_ec),
	path('disciplinas_gt', disciplinas_gt),
	path('disciplinas_jd', disciplinas_jd),
	path('disciplinas_rc', disciplinas_rc),
	path('disciplinas_si', disciplinas_si),
	path('disciplinas_adm_1s', disciplinas_adm_1s),
	path('disciplinas_adm_2s', disciplinas_adm_2s),
	path('disciplinas_adm_3s', disciplinas_adm_3s),
	path('disciplinas_adm_4s', disciplinas_adm_4s),
	path('disciplinas_adm_5s', disciplinas_adm_5s),
	path('disciplinas_adm_6s', disciplinas_adm_6s),
	path('disciplinas_adm_7s', disciplinas_adm_7s),
	path('disciplinas_adm_8s', disciplinas_adm_8s),
	path('disciplinas_ads_1s', disciplinas_ads_1s),
	path('disciplinas_ads_2s', disciplinas_ads_2s),
	path('disciplinas_ads_3s', disciplinas_ads_3s),
	path('disciplinas_ads_4s', disciplinas_ads_4s),
	path('disciplinas_ads_ead_1s', disciplinas_ads_ead_1s),
	path('disciplinas_ads_ead_2s', disciplinas_ads_ead_2s),
	path('disciplinas_ads_ead_3s', disciplinas_ads_ead_3s),
	path('disciplinas_ads_ead_4s', disciplinas_ads_ead_4s),
	path('disciplinas_ec_1s', disciplinas_ec_1s),
	path('disciplinas_ec_2s', disciplinas_ec_2s),
	path('disciplinas_ec_3s', disciplinas_ec_3s),
	path('disciplinas_ec_4s', disciplinas_ec_4s),
	path('disciplinas_ec_5s', disciplinas_ec_5s),
	path('disciplinas_ec_6s', disciplinas_ec_6s),
	path('disciplinas_ec_7s', disciplinas_ec_7s),
	path('disciplinas_ec_8s', disciplinas_ec_8s),
	path('disciplinas_gt_1s', disciplinas_gt_1s),
	path('disciplinas_gt_2s', disciplinas_gt_2s),
	path('disciplinas_gt_3s', disciplinas_gt_3s),
	path('disciplinas_gt_4s', disciplinas_gt_4s),
	path('disciplinas_gt_5s', disciplinas_gt_5s),
	path('disciplinas_gt_6s', disciplinas_gt_6s),
	path('disciplinas_gt_7s', disciplinas_gt_7s),
	path('disciplinas_gt_8s', disciplinas_gt_8s),
	path('disciplinas_jd_1s', disciplinas_jd_1s),
	path('disciplinas_jd_2s', disciplinas_jd_2s),
	path('disciplinas_jd_3s', disciplinas_jd_3s),
	path('disciplinas_jd_4s', disciplinas_jd_4s),
	path('disciplinas_si_1s', disciplinas_rc_1s),
	path('disciplinas_si_2s', disciplinas_rc_2s),
	path('disciplinas_si_3s', disciplinas_rc_3s),
	path('disciplinas_si_4s', disciplinas_rc_4s),
	path('disciplinas_si_1s', disciplinas_si_1s),
	path('disciplinas_si_2s', disciplinas_si_2s),
	path('disciplinas_si_3s', disciplinas_si_3s),
	path('disciplinas_si_4s', disciplinas_si_4s),
	path('disciplinas_si_5s', disciplinas_si_5s),
	path('disciplinas_si_6s', disciplinas_si_6s),
	path('disciplinas_si_7s', disciplinas_si_7s),
	path('disciplinas_si_8s', disciplinas_si_8s),
    path('admin', admin.site.urls),
]
