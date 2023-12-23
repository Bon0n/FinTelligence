from django.db import models
from django.utils import timezone


class Institution(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=15, default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_institution')

    def __str__(self):
        return self.name


class Card(models.Model):
    institution = models.ForeignKey('Institution', related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    credit_limit = models.DecimalField(max_digits=15, default=0)
    payment_date = models.DateTimeField()


class Debt(models.Model):
    card = models.ForeignKey('Card', related_name='debts', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    value = models.DecimalField(max_digits=15)
    installments = models.SmallIntegerField(max_length=3)
    current_installment = models.SmallIntegerField(max_length=3)


'''
class Finances(models.Model):
    name = models.CharField(max_length=15)
'''
