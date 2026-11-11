from django.contrib import admin
from .models import *


class FilmeAtorInline(admin.TabularInline):
    model = FilmeAtor
    extra = 1


class PaisInline(admin.TabularInline):
    model = Pais
    extra = 1


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    inlines = [FilmeAtorInline]


@admin.register(Continente)
class ContinenteAdmin(admin.ModelAdmin):
    inlines = [PaisInline]
    

class SerieEpisodioInline(admin.TabularInline):
    model = SerieEpisodio
    extra = 1

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    inlines = [SerieEpisodioInline]   



admin.site.register(Genero)
admin.site.register(Pais)
admin.site.register(Diretor)
admin.site.register(Ator)
admin.site.register(Temporada)
admin.site.register(Episodio)