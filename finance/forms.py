from django import forms
from finance.models import Institution


class InstitutionForm(forms.ModelForm):
    class META:
        model = Institution
        fields = ('name', 'balance', 'thumb')
        widgets = {
            'name': forms.TextInput(),
            'balance': forms.DecimalField(),
            'image': forms.ImageField()
        }
