from django.shortcuts import render
from django.views.generic import FormView, CreateView

from .forms import InstitutionForm


# Create your views here.
class Home(CreateView):
    template_name = 'home/index.html'
    form_class = InstitutionForm
