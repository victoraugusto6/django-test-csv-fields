from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    endereco_ip = models.GenericIPAddressField(null=True)
    mensagem = models.TextField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
