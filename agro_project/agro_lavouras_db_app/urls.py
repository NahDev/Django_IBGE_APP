from django.urls import path
from . import views

app_name = "agro_lavouras_db_app"  # Substitua 'sua_app_name' pelo nome da sua aplicação

urlpatterns = [
    path("categorias/", views.CategoriasListView.as_view(), name="categorias-list"),
    path(
        "categorias/<int:pk>/",
        views.CategoriasDetailView.as_view(),
        name="categorias-detail",
    ),
    path(
        "informacoes_gerais/",
        views.InformacoesGeraisListView.as_view(),
        name="informacoes_gerais-list",
    ),
    path(
        "informacoes_gerais/<int:pk>/",
        views.InformacoesGeraisDetailView.as_view(),
        name="informacoes_gerais-detail",
    ),
    path(
        "serie_detalhes/",
        views.SerieDetalhesListView.as_view(),
        name="serie_detalhes-list",
    ),
    path(
        "serie_detalhes/<int:pk>/",
        views.SerieDetalhesDetailView.as_view(),
        name="serie_detalhes-detail",
    ),
]
