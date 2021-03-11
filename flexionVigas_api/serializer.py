from rest_framework import serializers
from .models import VigaRectangular

class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model=VigaRectangular
        fields='__all__'


