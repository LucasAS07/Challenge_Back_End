from rest_framework import viewsets, generics, filters
from rest_framework import serializers
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from financas.models import Receita, Despesa
from financas.serialaizer import ReceitaSerialaizer, DespesaSerialaizer, ListagemDespesas, ListagemReceitas


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibe todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerialaizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao_receita']


class DespesasViewSet(viewsets.ModelViewSet):
    """Exibe todas as despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerialaizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao_despesa']


class ListaDespesas(generics.ListAPIView):
    """Exibe as despesas por determinado mes e ano"""

    def get_queryset(self):
        queryset = Despesa.objects.filter(
            data_despesa__month=self.kwargs['month'], data_despesa__year=self.kwargs['year'])
        return queryset

    serializer_class = ListagemDespesas


class ListaReceitas(generics.ListAPIView):
    """Exibe as Receitas por determinado mes e ano"""

    def get_queryset(self):
        queryset = Receita.objects.filter(
            data_receita__month=self.kwargs['month'], data_receita__year=self.kwargs['year'])
        return queryset

    serializer_class = ListagemReceitas


class ResumoDoMes(APIView, serializers.ModelSerializer):
    """Exibe o relatorio do mes """

    def get(self, request, mes, ano):
        receita_do_mes = Receita.objects.filter(data_receita__month=mes, data_receita__year=ano).aggregate(
            Sum('valor_receita'))['valor_receita__sum'] or 0
        despesa_do_mes = Despesa.objects.filter(data_despesa__month=mes, data_despesa__year=ano).aggregate(
            Sum('valor_despesa'))['valor_despesa__sum'] or 0
        saldo = receita_do_mes - despesa_do_mes
        gasto_por_categoria = Despesa.objects.filter(
            data_despesa__month=mes, data_despesa__year=ano).annotate(valor_total=Sum('valor_despesa'))

        return Response({
            "Receita do Mês": f"R${receita_do_mes}",
            "Despesa do Mês": f"R${despesa_do_mes}",
            "Saldo Finasl do Mês": f"R${saldo}",
            "Gasto por Categoria": gasto_por_categoria
        })
