from django.urls import path

from finance.views import Home, CreateInstitution

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('home/create_institution', CreateInstitution.as_view(), name='create_institution')
]