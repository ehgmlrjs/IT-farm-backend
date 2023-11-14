from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Cart
from django.shortcuts import get_object_or_404
from product.models import Product

class CartCreateView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)

class CartUpdateView(APIView):
    def post(self, request):
        try:
            pk = request.data.get('cart_id')
            cart = get_object_or_404(Cart, pk=pk)
            product_id = request.data.get('product_id')
            product = get_object_or_404(Product, pk=product_id)
            if request.data.get('type'):
                if product.count <= cart.count:
                    return Response({'message':'재고 x'}, status=status.HTTP_404_NOT_FOUND)
                count = cart.count + 1
            elif cart.count>0:
                count = cart.count -1
            cart.count = count
            cart.save()
            return Response({'message':'성공'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':f'실패: {e}'}, status=status.HTTP_400_BAD_REQUEST)
    
class CartDeleteView(APIView):
    def delete(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id)
        try:
            cart.delete()
            return Response({'message':'삭제'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':f'삭제 실패: {e}'}, status=status.HTTP_400_BAD_REQUEST)

class CartReadView(APIView):
    def get(self, request):
        user_id = request.member.get('id')
        cart = Cart.objects.filter(user_id=user_id)
        serializer = CartReadSerializer(cart,many=True)
        return Response(serializer.data)