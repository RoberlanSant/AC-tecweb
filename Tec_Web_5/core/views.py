from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, "index.html")

def lista_de_cursos(request):
	return render(request, "lista_de_cursos.html")

def adm(request):
	return render(request, "adm.html")

def ads(request):
	return render(request, "ads.html")

def adsead(request):
	return render(request, "adsead.html")

def bancodedados(request):
	return render(request, "bancodedados.html")

def detalhe_de_curso(request):
	return render(request, "detalhe_de_curso.html")

def eng_comput(request):
	return render(request, "eng_comput.html")

def gestao_ti(request):
	return render(request, "gestao_ti.html")

def jogos_digitais(request):
	return render(request, "jogos_digitais.html")

def noticias(request):
	return render(request, "noticias.html")

def processos_gerenciais(request):
	return render(request, "processos_gerenciais.html")

def producao_multimedia(request):
	return render(request, "producao_multimedia.html")

def redes_computadores(request):
	return render(request, "redes_computadores.html")

def si(request):
	return render(request, "si.html")

