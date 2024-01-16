from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView

from .forms import InstitutionForm, CardForm, DebtForm
from .models import Institution


# Create your views here.
class CreateInstitution(CreateView):
    form_class = InstitutionForm
    template_name = 'home/create_institution.html'
    success_url = 'home/index.html'


class CreateCard(CreateView):
    form_class = CardForm
    template_name = 'home/create_card.html'
    success_url = 'home/index.html'


class CreateDebt(CreateView):
    form_class = DebtForm
    template_name = 'home/create_debt.html'
    success_url = 'home/index.html'


class Home(ListView):
    model = Institution
    template_name = 'home/index.html'

    def get_queryset(self):
        return Institution.objects.filter(user=self.request.user)


class InstitutionDetails(UpdateView):
    form_class = InstitutionForm
    model = Institution
    template_name = 'home/detail.html'
    success_url = reverse_lazy('home/index.html')
