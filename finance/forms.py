from django import forms
from .models import Institution, Card, Debt, UserDetail, RecurringDebt


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('incoming',)
        widgets = {
            'incoming': forms.TextInput()
        }


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ('name', 'balance', 'image')
        widgets = {
            'name': forms.Select(),
            'balance': forms.NumberInput(),
            'image': forms.FileInput(),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('institution', 'name', 'credit_limit', 'payment_date')
        widgets = {
            'institution': forms.Select(),
            'name': forms.TextInput(),
            'credit_limit': forms.NumberInput(),
            'payment_date': forms.DateInput(),
        }


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ('card', 'name', 'category', 'description', 'value', 'installments', 'buy_date')
        widgets = {
            'card': forms.Select(),
            'name': forms.TextInput(),
            'category': forms.TextInput(),
            'description': forms.TextInput(),
            'value': forms.NumberInput(),
            'installments': forms.NumberInput(),
            'buy_date': forms.NumberInput(),
        }


class RecurringDebtForm(forms.ModelForm):
    class Meta:
        model = RecurringDebt
        fields = ('name', 'category', 'description', 'value', 'recurrence_time_in_months')
        widgets = {
            'name': forms.TextInput(),
            'category': forms.TextInput(),
            'description': forms.TextInput(),
            'value': forms.NumberInput(),
            'recurrence_time_in_months': forms.NumberInput(),
        }
