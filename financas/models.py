from django.db import models


class Receita(models.Model):
    descricao_receita = models.CharField(max_length=100)
    valor_receita = models.DecimalField(max_digits=19, decimal_places=2)
    data_receita = models.DateField()

    def __str__(self):
        return self.descricao_receita

class Despesa(models.Model):
    descricao_despesa = models.CharField(max_length=100)
    valor_despesa = models.DecimalField(max_digits=19, decimal_places=2)
    data_despesa = models.DateField()

    def __str__(self):
        return self.descricao_despesa