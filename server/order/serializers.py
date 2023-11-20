from .models import Order, Review
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewUPdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review_id', 'content', 'score')

class ReviewReadSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='order_id.user_id.nickname', read_only=True)

    class Meta:
        model = Review
        fields = ('review_id','order_id','product_name','content','score','photo','regdate','nickname')