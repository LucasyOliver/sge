from django import forms
from . import models

class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name','description',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name','description',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title','brand','category','serie_number','cost_price','selling_price','description',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'title': 'Nome',
            'brand': 'Marca',
            'category': 'Categoria',
            'serie_number': 'Número de serie',
            'cost_price': 'Preço de custo',
            'selling_price': 'Preço de venda',
            'description': 'Descrição',
        }