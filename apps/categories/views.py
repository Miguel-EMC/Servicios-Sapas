from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategorySerializer
from apps.services.models import Category

# Create your views here.
class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    