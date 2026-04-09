from django import forms
from .models import Cliente, Compra, Pagamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'descricao_produto', 'valor', 'data']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'descricao_produto': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'cliente': 'Cliente',
            'descricao_produto': 'Produto',   
            'valor': 'Valor',
            'data': 'Data da Compra',
        }


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['cliente', 'data', 'valor']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
        labels = {
            'cliente': 'Cliente',
            'data': 'Data do Pagamento',
            'valor': 'Valor Pago',
        }