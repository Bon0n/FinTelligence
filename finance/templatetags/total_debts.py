import datetime

from django import template
from django.db.models import Sum

from finance.models import Debt

register = template.Library()


@register.simple_tag
def total_of_debts(card_id):
    value = Debt.objects.filter(card_id=card_id).aggregate(Sum('value'))['value__sum']
    if value != None:
        return value
    return 'Não há gastos aqui'


@register.simple_tag
def current_installment(debt_id):
    debt = Debt.objects.get(id=debt_id)
    current = int((datetime.date.today() - debt.buy_date).days / 30)
    if current <= 0:
        return 1
    return current
