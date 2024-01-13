from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView

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
