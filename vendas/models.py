from django.db import models
from decimal import Decimal

class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    descricao_produto = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    class Meta:
        ordering = ['-data']


class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagamentos')
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-data']