from django.shortcuts import render
from rest_framework import generics
from finance.models import Institution
from finance_api.serializers import InstitutionSerializer


# Create your views here.

class InstitutionList(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
