from django.db import models

class RelatorioEstoque(models.Model):
    id_produto = models.IntegerField()
    nome = models.CharField(max_length=255)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} - {self.id_produto}'