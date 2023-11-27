from django.test import TestCase
from .models import Categorias, InformacoesGerais, SerieDetalhes


class CategoriasModelTest(TestCase):
    def setUp(self):
        self.categoria = Categorias.objects.create(id=1, nome="Categoria de Teste")

    def test_categoria_id(self):
        self.assertEqual(self.categoria.id, 1)

    def test_categoria_nome(self):
        self.assertEqual(self.categoria.nome, "Categoria de Teste")


class InformacoesGeraisModelTest(TestCase):
    def setUp(self):
        self.informacao = InformacoesGerais.objects.create(
            id=1, variavel="Variavel de Teste", unidade="Unidade de Teste"
        )

    def test_informacao_id(self):
        self.assertEqual(self.informacao.id, 1)

    def test_informacao_variavel(self):
        self.assertEqual(self.informacao.variavel, "Variavel de Teste")

    def test_informacao_unidade(self):
        self.assertEqual(self.informacao.unidade, "Unidade de Teste")


class SerieDetalhesModelTest(TestCase):
    def setUp(self):
        categoria = Categorias.objects.create(id=1, nome="Categoria de Teste")
        informacao = InformacoesGerais.objects.create(
            id=1, variavel="Variavel de Teste", unidade="Unidade de Teste"
        )
        self.serie = SerieDetalhes.objects.create(
            informacoes_gerais=informacao,
            localidade_id=1,
            localidade_nivel_id="Nível de Teste",
            localidade_nome="Localidade de Teste",
            serie_ano=2023,
            serie_valor=123.456,
            categorias=categoria,
        )

    def test_serie_informacoes_gerais(self):
        self.assertEqual(self.serie.informacoes_gerais.variavel, "Variavel de Teste")

    def test_serie_localidade_id(self):
        self.assertEqual(self.serie.localidade_id, 1)

    def test_serie_localidade_nivel_id(self):
        self.assertEqual(self.serie.localidade_nivel_id, "Nível de Teste")

    def test_serie_localidade_nome(self):
        self.assertEqual(self.serie.localidade_nome, "Localidade de Teste")

    def test_serie_ano(self):
        self.assertEqual(self.serie.serie_ano, 2023)

    def test_serie_valor(self):
        self.assertEqual(
            float(self.serie.serie_valor), 123.456
        )  # Converta para float para comparar

    def test_serie_categorias(self):
        self.assertEqual(self.serie.categorias.nome, "Categoria de Teste")
