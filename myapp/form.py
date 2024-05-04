from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date']


class ImageForm(forms.Form):
    image = forms.ImageField()
