from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ServiceSerializer
from apps.services.models import Service

# Create your views here.
class ServicesView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    