from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Product
from django.shortcuts import get_object_or_404
from django.db.models import Q


class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdateView(APIView):
    def post(self, request):
        pk = request.data.get('product_id')
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        try:
            product.delete()
            return Response({'message':'삭제'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':f'삭제 실패: {e}'}, status=status.HTTP_400_REQUEST)

class ProductReadView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
class ProductSearchView(APIView):
    def get(self, request, product_name):
        if product_name:
            products = Product.objects.filter(
                Q(name__icontains=product_name) |
                Q(kind__icontains=product_name)
                )
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)
        return Response({'message':'잘못된 검색어'}, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailReadView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)