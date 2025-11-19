from django import forms
from .models import Vaga, Empresa

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'empresa', 'descricao', 'localizacao', 'tipo','remoto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'remoto': forms.CheckboxInput(attrs={'class': 'switch-input'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VagaForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].queryset = Empresa.objects.all()

class FiltroForm(forms.Form):
    busca = forms.CharField(required=False, label='Buscar vaga')
    localizacao = forms.CharField(required=False, label='Localização')
    tipo = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('aprendiz', 'Jovem Aprendiz'),
            ('estagio', 'Estagiário'),
        ]
    )
    remoto = forms.BooleanField(
        required=False, 
        label='Remoto',
        widget=forms.CheckboxInput(attrs={'id': 'filtro_remoto'})
)

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'imagem', 'site']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.URLInput(attrs={'class': 'form-control'}),
        }