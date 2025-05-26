from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

# MODEL SIMPLES PARA ENTENDER COMO FUNCIONA UM TESTE EM DJANGO