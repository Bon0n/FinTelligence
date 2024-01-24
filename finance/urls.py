from django.urls import path

from finance.views import Home, CreateInstitution, InstitutionDetails, Login

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('home/create_institution', CreateInstitution.as_view(), name='create_institution'),
    path('home/details/<pk>', InstitutionDetails.as_view(), name='details'),
    path('', Login.as_view(), name='login')
]