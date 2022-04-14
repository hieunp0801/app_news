
from django import forms
from .models import *

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
        }