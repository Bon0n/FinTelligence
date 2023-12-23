from django.db import models
from django.utils import timezone


class Institution(models.Model):
    name = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=15, default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_institution')

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=15)

'''
class Finances(models.Model):
    name = models.CharField(max_length=15)
'''
