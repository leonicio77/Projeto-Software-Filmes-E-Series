from django.shortcuts import render
from django.views import View
from .models import Filme

class FilmesView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})
