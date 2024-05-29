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
    

class Subfilo(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    filo = models.ForeignKey(Filo, on_delete=models.CASCADE, related_name='subfilos')

    def __str__(self):
        return self.nome
    

class Especie(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    subfilo = models.ForeignKey(Subfilo, on_delete=models.CASCADE, related_name='especies')

    def __str__(self):
        return self.nome
