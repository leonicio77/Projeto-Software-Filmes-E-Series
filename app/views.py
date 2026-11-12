from django.shortcuts import render
from django.views import View
from .models import *

class FilmesView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})

class SeriesView(View):
    def get(self, request, *args, **kwargs):
        series = Serie.objects.all()
        return render(request, 'series.html', {'series': series})    

class AtoresView(View):
    def get(self, request, *args, **kwargs):
        atores = Ator.objects.all()
        return render(request, 'atores.html', {'atores': atores})   

class DiretoresView(View):
    def get(self, request, *args, **kwargs):
        diretores = Diretor.objects.all()
        return render(request, 'diretores.html', {'diretores': diretores})   

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html',{'generos': generos})   

class PaisesView(View):
    def get(self, request, *args, **kwargs):
        paises = Pais.objects.all()
        return render(request, 'paises.html', {'paises': paises})       

class ContinentesView(View):
    def get(self, request, *args, **kwargs):
        continentes = Continente.objects.all()
        return render(request, 'continentes.html', {'continentes': continentes})     

class TemporadasView(View):
    def get(self, request, *args, **kwargs):
        temporadas = Temporada.objects.all()
        return render(request, 'temporadas.html', {'temporadas': temporadas})      

class EpisodiosView(View):
    def get(self, request, *args, **kwargs):
        episodios = Episodio.objects.all()
        return render(request, 'episodios.html', {'episodios': episodios})         

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
