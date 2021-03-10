from rest_framework import serializers
from .models import VigaRectangular

class VigaSerializer(serializers.Serializer):
    class Meta:
        model=VigaRectangular
        fields='__all__'


