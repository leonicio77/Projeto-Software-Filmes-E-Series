from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Continente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Continente"
        verbose_name_plural = "Continentes"        

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE, verbose_name="Continente", null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países" 

class Diretor(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    site = models.CharField(max_length=200, blank=True, verbose_name="Site")
    insta = models.CharField(max_length=200, blank=True, verbose_name="Instagram")
    face = models.CharField(max_length = 200, blank=True, verbose_name="Facebook") 
    twitter = models.CharField(max_length = 200, blank=True, verbose_name="Twitter")
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, verbose_name="Nacionalidade")
    def __str__(self):
        return self.nome

    class Meta:        
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"

class Filme(models.Model):
    nome = models.CharField(max_length=150)
    duracao = models.IntegerField(verbose_name="Duração (min)")
    sinopse = models.TextField()
    site_oficial = models.CharField(max_length=200, blank=True)
    data_lancamento = models.DateField(verbose_name="Data de lançamento")
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País")
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE,)
    def __str__(self):
        return self.nome
   
    class Meta:
       verbose_name = "Filme"
       verbose_name_plural = "Filmes"  


class Ator(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome")
    site = models.CharField(max_length=200, blank=True, verbose_name="site")
    insta = models.CharField(max_length=100, blank=True, verbose_name="Instagram")
    face = models.CharField(max_length=100, blank=True, verbose_name="Facebook")
    twitter = models.CharField(max_length=100, blank=True, verbose_name="Twitter")
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Nacionalidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"

class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, verbose_name="Filme")
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE, verbose_name="Ator")

    def __str__(self):
        return f"{self.filme} - {self.ator}"

    class Meta:
        verbose_name = "Ator do filme"
        verbose_name_plural = "Atores do filme"

class Serie(models.Model):
    nome = models.CharField(max_length=150)
    duracao = models.IntegerField(verbose_name="Duração (min)")
    sinopse = models.TextField()
    site_oficial = models.CharField(max_length=200, blank=True)
    data_lancamento = models.DateField(verbose_name="Data de lançamento")
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País")
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
   
    class Meta:
       verbose_name = "Série"
       verbose_name_plural = "Séries"     

class Temporada(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

class Episodio(models.Model):
    nome = models.CharField(max_length=150, verbose_name = "nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Episódio"
        verbose_name_plural = "Episódios"    


class SerieEpisodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Série")
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, verbose_name="Temporada")
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE, verbose_name="Episódio")
    duracao = models.IntegerField(verbose_name="Duração (min)")
    data_disponibilizacao = models.DateField(verbose_name="Data de disponibilização")

    def __str__(self):
        return f"{self.serie} - {self.temporada} - {self.episodio}"

    class Meta:
        verbose_name = "Episódio da série"
        verbose_name_plural = "Episódios da série"  







