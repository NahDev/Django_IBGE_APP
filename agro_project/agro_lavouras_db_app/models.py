# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class InformacoesGerais(models.Model):
    id = models.IntegerField(primary_key=True)
    variavel = models.CharField(max_length=255, blank=True, null=True)
    unidade = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacoes_gerais'


class SerieDetalhes(models.Model):
    informacoes_gerais = models.ForeignKey(InformacoesGerais, models.DO_NOTHING, blank=True, null=True)
    localidade_id = models.IntegerField(blank=True, null=True)
    localidade_nivel_id = models.CharField(max_length=255, blank=True, null=True)
    localidade_nome = models.CharField(max_length=255, blank=True, null=True)
    serie_ano = models.IntegerField(blank=True, null=True)
    serie_valor = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_detalhes'
