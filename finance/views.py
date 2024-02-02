from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView
from .forms import InstitutionForm, CardForm, DebtForm, UserDetailForm, RecurringDebtForm
from .models import Institution


class Login(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Credenciais inválidas.')
        return self.render_to_response(self.get_context_data(form=form))


# Create your views here.
class CreateInstitution(CreateView):
    form_class = InstitutionForm
    template_name = 'create/create_institution.html'
    success_url = reverse_lazy('lists/general.html')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateCard(CreateView):
    form_class = CardForm
    template_name = 'create/create_card.html'
    success_url = reverse_lazy('home/index.html')


class CreateDebt(CreateView):
    form_class = DebtForm
    template_name = 'create/create_debt.html'
    success_url = reverse_lazy('home/index.html')


class CreateRecurringDebt(CreateView):
    form_class = RecurringDebtForm
    template_name = 'create/create_debt.html'
    success_url = reverse_lazy('home/index.html')


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


class GeneralListView(ListView):
    model = Institution
    template_name = 'lists/general.html'
    context_object_name = 'institutions'

    def get_queryset(self):
        return Institution.objects.filter(user=self.request.user)


class UserUpdateView(UpdateView):
    form_class = UserDetailForm
