from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Pest
from django.shortcuts import get_object_or_404


class PestCreateView(APIView):
    def post(self, request):
        serializer = PestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)

class PestUpdateView(APIView):
    def post(self, request):
        pk = request.data.get('pest_id')
        pest = get_object_or_404(Pest, pk=pk)
        serializer = PestSerializer(instance=pest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)
    
class PestDeleteView(APIView):
    def delete(self, request, pest_id):
        pest = get_object_or_404(Pest, id=pest_id)
        try:
            pest.delete()
            return Response({'message':'삭제'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':f'삭제 실패: {e}'},status=status.HTTP_400_BAD_REQUEST)

class PestReadView(APIView):
    def get(self, request, farm_id):
        pest = Pest.objects.filter(farm_id=farm_id)
        serializer = PestSerializer(pest,many=True)
        return Response(serializer.data)
    
class PestSolutionView(APIView):
    def put(self, request):
        try:
            pk = request.data.get('pest_id')
            pest = get_object_or_404(Pest, pk=pk)
            pest.solution = request.data.get('solution')
            pest.save()
            return Response({'message':'성공'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':f'실패: {e}'}, status=status.HTTP_400_BAD_REQUEST)