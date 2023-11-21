from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SpaSerializer
from apps.spas.models import Spa

# Create your views here.
class SpasView(viewsets.ModelViewSet):
    serializer_class = SpaSerializer
    queryset = Spa.objects.all()
    