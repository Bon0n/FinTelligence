from django import forms
from .models import Institution


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ('name', 'balance', 'image')
        widgets = {
            'name': forms.Select(),
            'balance': forms.NumberInput(),
            'image': forms.FileInput(),
        }
