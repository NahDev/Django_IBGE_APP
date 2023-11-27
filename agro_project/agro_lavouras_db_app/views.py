from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Categorias, InformacoesGerais, SerieDetalhes


class CategoriasListView(ListView):
    model = Categorias
    template_name = "agro_lavouras_db_app/categorias_list.html"  # Crie o arquivo HTML correspondente


class CategoriasDetailView(DetailView):
    model = Categorias
    template_name = "agro_lavouras_db_app/categorias_detail.html"  # Crie o arquivo HTML correspondente


class InformacoesGeraisListView(ListView):
    model = InformacoesGerais
    template_name = "agro_lavouras_db_app/informacoes_gerais_list.html"  # Crie o arquivo HTML correspondente


class InformacoesGeraisDetailView(DetailView):
    model = InformacoesGerais
    template_name = "agro_lavouras_db_app/informacoes_gerais_detail.html"  # Crie o arquivo HTML correspondente


class SerieDetalhesListView(ListView):
    model = SerieDetalhes
    template_name = "agro_lavouras_db_app/serie_detalhes_list.html"  # Crie o arquivo HTML correspondente


class SerieDetalhesDetailView(DetailView):
    model = SerieDetalhes
    template_name = "agro_lavouras_db_app/serie_detalhes_detail.html"  # Crie o arquivo HTML correspondente
