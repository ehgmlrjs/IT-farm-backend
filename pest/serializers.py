from .models import Pest
from rest_framework import serializers


class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = '__all__'
    