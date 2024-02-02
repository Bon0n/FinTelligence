from django.urls import path

from finance.views import Home, CreateInstitution, InstitutionDetails, Login, GeneralListView, CreateDebt, CreateCard

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('create/create_institution', CreateInstitution.as_view(), name='create_institution'),
    path('create/create_card', CreateCard.as_view(), name='create_card'),
    path('create/create_debt', CreateDebt.as_view(), name='create_debt'),
    path('home/details/<pk>', InstitutionDetails.as_view(), name='details'),
    path('general', GeneralListView.as_view(), name='general'),
    path('', Login.as_view(), name='login')
]