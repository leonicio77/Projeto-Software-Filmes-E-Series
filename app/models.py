from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Meta:
        verbose_name = "Genêro"
        verbose_name_plural = "Genêros"

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países" 

class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome 
class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"


class Filme(models.Model):
    nome = models.CharField(max_length=150)
    duracao = models.IntegerField()
    sinopse = models.TextField()
    site_oficial = models.CharField(max_length=200, blank=True)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
class Meta:
    verbose_name = "Filme"
    verbose_name_plural = "Filmes"        


