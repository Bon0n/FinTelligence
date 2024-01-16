from django.contrib import admin
from .models import Institution, Card, Debt, UserDetail

# Register your models here.
admin.site.register(Institution)
admin.site.register(Card)
admin.site.register(Debt)
admin.site.register(UserDetail)
