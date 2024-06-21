from django.db import models

class BaseModel(models.Model):
    nome = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    
    descricao = models.CharField(
        max_length=2555,
        default=""
    )
    
    imagem = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True

class Reino(BaseModel):
    pass

class Filo(BaseModel):
    reino = models.ForeignKey(Reino, on_delete=models.CASCADE, related_name='filos')

class Classe(BaseModel):
    filo = models.ForeignKey(Filo, on_delete=models.CASCADE, related_name='classes')

class Ordem(BaseModel):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='ordens')

class Familia(BaseModel):
    ordem = models.ForeignKey(Ordem, on_delete=models.CASCADE, related_name='familias')

class Genero(BaseModel):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='generos')

class Especie(BaseModel):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='especies')

