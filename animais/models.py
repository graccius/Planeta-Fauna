from django.db import models

class Reino(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='reinos/')

    def __str__(self):
        return self.nome


class Filo(models.Model):
    nome = models.CharField(max_length=100)
    reino = models.ForeignKey(Reino, on_delete=models.CASCADE, related_name='filos')

    def __str__(self):
        return self.nome
    
class Subfilo(models.Model):
    nome = models.CharField(max_length=100)
    filo = models.ForeignKey(Filo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Especie(models.Model):
    nome = models.CharField(max_length=100)
    subfilo = models.ForeignKey(Subfilo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
