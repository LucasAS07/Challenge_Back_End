from django.db import models


def receita_filtro_descricao(descricao):
    return Receita.objects.filter(descricao=descricao).exists()


class Receita(models.Model):
    descricao_receita = models.CharField(max_length=100)
    valor_receita = models.FloatField()
    data_receita = models.DateField()


def despesa_filtro_descricao(descricao):
    return Despesa.objects.filter(descricao=descricao).exists()


class Despesa(models.Model):
    CATEGORIA = (
        ('A', 'Outros'),
        ('S', 'Saude'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevistos'),
        ('O', 'Outros'),
    )
    descricao_despesa = models.CharField(max_length=100)
    valor_despesa = models.FloatField()
    data_despesa = models.DateField()
    categoria = models.CharField(
        max_length=1, choices=CATEGORIA, blank=False, null=False, default='O')

    def __str__(self):
        return self.descricao_despesa
