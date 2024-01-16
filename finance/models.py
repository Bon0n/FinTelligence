from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

INSTITUTION_LIST = [
    ('BRADESCO', 'Bradesco'),
    ('C6', 'C6'),
    ('INTER', 'Inter'),
    ('ITAU', 'Itaú'),
    ('NUBANK', 'NuBank'),
    ('SANTANDER', 'Santander'),
]


class UserDetail(models.Model):
    user = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    incoming = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Renda')


class Institution(models.Model):
    user = models.ForeignKey(User, related_name='institutions', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=INSTITUTION_LIST, verbose_name='Nome da Instituição')
    balance = models.DecimalField(max_digits=15, default=0, decimal_places=2, verbose_name='Saldo')
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='img_institution', verbose_name='Imagem da Instituição', null=True, blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    institution = models.ForeignKey(Institution, related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    credit_limit = models.DecimalField(max_digits=15, default=0, decimal_places=2)
    payment_date = models.DateField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


INSTALLMENTS_LIST = [
    (1, '1x'),
    (2, '2x'),
    (3, '3x'),
    (4, '4x'),
    (5, '5x'),
    (6, '6x'),
    (7, '7x'),
    (8, '8x'),
    (9, '9x'),
    (10, '10x'),
    (11, '11x'),
    (12, '12x'),
]


class Debt(models.Model):
    card = models.ForeignKey('Card', related_name='debts', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    installments = models.SmallIntegerField(choices=INSTALLMENTS_LIST)
    current_installment = models.SmallIntegerField()
    creation_date = models.DateTimeField(default=timezone.now)


'''
class Finances(models.Model):
    name = models.CharField(max_length=15)
'''
