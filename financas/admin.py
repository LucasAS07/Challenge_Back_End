from django.contrib import admin
from financas.models import Receita, Despesa


class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao_receita', 'valor_receita', 'data_receita')
    list_display_links = ('id', 'descricao_receita')
    search_fields = ('descricao_receita',)
    list_per_page = 15


admin.site.register(Receita, Receitas)


class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao_despesa', 'valor_despesa', 'data_despesa')
    list_display_links = ('id', 'descricao_despesa')
    search_fields = ('descricao_despesa',)
    list_per_page = 15


admin.site.register(Despesa, Despesas)
