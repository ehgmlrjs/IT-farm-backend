from .models import Farms
from rest_framework import serializers


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = '__all__'
    