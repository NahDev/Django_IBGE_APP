from django import forms
from .models import Categorias, InformacoesGerais, SerieDetalhes

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'

class InformacoesGeraisForm(forms.ModelForm):
    class Meta:
        model = InformacoesGerais
        fields = '__all__'

class SerieDetalhesForm(forms.ModelForm):
    class Meta:
        model = SerieDetalhes
        fields = '__all__'
