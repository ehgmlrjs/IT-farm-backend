from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
    
class CartReadSerializer(serializers.ModelSerializer):
    # farm_name = serializers.CharField(source='farm_id.name', read_only=True)
    # farm_address = serializers.CharField(source='farm_id.address', read_only=True)

    class Meta:
        model = Cart
        fields = ['id','user_id', 'count', 'product_id', 'created_at', 'updated_at']