from .models import Farm_products
from rest_framework import serializers


class FarmProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm_products
        fields = '__all__'
    
class FarmReadSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm_id.name', read_only=True)
    farm_address = serializers.CharField(source='farm_id.address', read_only=True)

    class Meta:
        model = Farm_products
        fields = ['id','farm_id', 'eco', 'kind', 'crop', 'center', 'state', 'created_at', 'updated_at','farm_name','farm_address']