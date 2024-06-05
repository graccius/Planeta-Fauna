from django.db import models

class Reino(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    imagem = models.ImageField(upload_to='reinos/')

    def __str__(self):
        return self.nome


class Filo(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    reino = models.ForeignKey(Reino, on_delete=models.CASCADE, related_name='filos')

    def __str__(self):
        return self.nome
    
class Classe(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    filo = models.ForeignKey(Filo, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.nome


class Ordem(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='ordens')

    def __str__(self):
        return self.nome


class Familia(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    ordem = models.ForeignKey(Ordem, on_delete=models.CASCADE, related_name='familias')

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=True,
        max_length=50
    )
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='generos')

    def __str__(self):
        return self.nome


class Especie(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='especies')

    def __str__(self):
        return self.nome

