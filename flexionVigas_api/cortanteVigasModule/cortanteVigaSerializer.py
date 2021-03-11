from math import trunc
from rest_framework import serializers


class cortanteVigaSerializer(serializers.Serializer):
    bw = serializers.FloatField(required=True)
    hw = serializers.FloatField(required=True)
    r = serializers.FloatField(required=True)
    fc = serializers.FloatField(required=True)
    fy = serializers.FloatField(required=True)
    d = serializers.FloatField(required=True)
    phiVc = serializers.FloatField(required=False)
    phiVs = serializers.FloatField(required=False)
    phiVn = serializers.FloatField(required=False)
    phiVsMax = serializers.FloatField(required=False)
    phiVnMax = serializers.FloatField(required=False)
    asCortante = serializers.FloatField(required=True)
    separacionAs = serializers.FloatField(required=True)
    Vu = serializers.FloatField(required=False)

    def is_valid(self, raise_exception):
        
        return super().is_valid(raise_exception=raise_exception)

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
