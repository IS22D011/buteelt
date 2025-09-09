from django import forms
from .models import Baraa, Angilal

class BaraaForm(forms.ModelForm):
    class Meta:
        model=Baraa
        fields='__all__'
        labels={
            'name':'Нэр',
            'category':'Ангилал'
        }