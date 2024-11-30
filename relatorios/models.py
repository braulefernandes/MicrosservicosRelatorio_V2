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
    

class RelatorioVenda(models.Model):
    id_venda = models.IntegerField(unique=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField()

    def __str__(self):
        return f'Venda {self.id_venda} - {self.data_venda}'
    
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(RelatorioVenda, on_delete=models.CASCADE, related_name="itens_venda")
    produto_id = models.IntegerField()  # ID do produto relacionado
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Produto {self.produto_id} na Venda {self.venda.id_venda}'