from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView

from .forms import InstitutionForm
from .models import Institution


# Create your views here.
class CreateInstitution(CreateView):
    form_class = InstitutionForm
    template_name = 'home/create_institution.html'
    success_url = 'home/index.html'


class Home(ListView):
    model = Institution
    template_name = 'home/index.html'

class InstitutionDetails(UpdateView):
    form_class = InstitutionForm
    model = Institution
    template_name = 'home/detail.html'
    success_url = reverse_lazy('home/index.html')