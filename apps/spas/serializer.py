from rest_framework import serializers
from .models import Spa

class SpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spa
        fields = '__all__'