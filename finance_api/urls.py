from django.urls import path

from . import views

urlpatterns = [
    path('institution/', views.InstitutionList.as_view()),
]
