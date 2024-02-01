from django.urls import path

from finance.views import Home, CreateInstitution, InstitutionDetails, Login, InstitutionsList

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('create/create_institution', CreateInstitution.as_view(), name='create_institution'),
    path('home/details/<pk>', InstitutionDetails.as_view(), name='details'),
    path('institutions', InstitutionsList.as_view(), name='institutions'),
    path('', Login.as_view(), name='login')
]