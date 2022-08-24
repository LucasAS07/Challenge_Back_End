from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitasViewSet, DespesasViewSet, ListaDespesas, ListaReceitas, ResumoDoMes
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Carteira Virtual",
        default_version='v1',
        description="Controle de finanças pessoais",
        terms_of_service="#",
        contact=openapi.Contact(email="lucas-oliveira25@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('despesas/<int:month>/<int:year>/', ListaDespesas.as_view()),
    path('receitas/<int:month>/<int:year>/', ListaReceitas.as_view()),
    path('resumo/<int:mes>/<int:ano>/', ResumoDoMes.as_view()),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
