from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('series/', SeriesView.as_view(), name='series'),
    path('atores/', AtoresView.as_view(), name='atores'),
    path('diretores/', DiretoresView.as_view(), name='diretores'),
    path('generos/', GenerosView.as_view(), name='generos'),
    path('paises/', PaisesView.as_view(), name='generos'),
    path('continentes/', ContinentesView.as_view(), name='continentes'),
    path('temporadas/', TemporadasView.as_view(), name='temporadas'),
    path('episodios/', EpisodiosView.as_view(), name='episodios'),
]
