from rest_framework import serializers

class cortanteVigaSerializer(serializers.Serializer):
    bw = serializers.FloatField()
    hw = serializers.FloatField()
    r = serializers.FloatField()
    fc = serializers.FloatField()
    fy = serializers.FloatField()
    d = serializers.FloatField()
    phiVc=serializers.FloatField(required=False)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)