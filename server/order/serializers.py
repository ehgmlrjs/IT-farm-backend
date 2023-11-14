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
        fields = ('review_id', 'content', 'photo', 'score')