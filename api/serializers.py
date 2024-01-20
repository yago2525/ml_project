from rest_framework import serializers


class HousePricePredictSerializer(serializers.Serializer):
    zn = serializers.FloatField()
    rm = serializers.FloatField()
    dis = serializers.FloatField()
    chas = serializers.FloatField()
