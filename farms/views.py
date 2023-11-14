from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Farms
from django.shortcuts import get_object_or_404
from .distance import geocoding, distance


class FarmCreateView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        address = request.data.get('address')
        address_detail = request.data.get('address_detail')
        farms = Farms.objects.filter(user_id=user_id,address=address,address_detail=address_detail)
        if farms.exists():
            return Response({"message":"이미 등록된 농장입니다."}, status=status.HTTP_409_CONFLICT)
        latitude, longitude = geocoding(address)
        center = distance(latitude,longitude)
        serializer = FarmSerializer(data={**request.data, 'user_id':user_id, 'center':center, 'latitude':latitude, 'longitude':longitude})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)

class FarmUpdateView(APIView):
    def post(self, request):
        pk = request.member.get('id')
        farm = get_object_or_404(Farms, pk=pk)
        user_id = request.data.get('user_id')
        address = request.data.get('address')
        latitude, longitude = geocoding(address)
        center = distance(latitude,longitude)
        serializer = FarmSerializer(instance=farm, data={**request.data, 'user_id':user_id, 'center':center, 'latitude':latitude, 'longitude':longitude})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        return Response({"message": "실패", "error": errors}, status=status.HTTP_400_BAD_REQUEST)
    
class FarmDeleteView(APIView):
    def post(self, request, farm_id):
        farm = get_object_or_404(Farms, id=farm_id)
        try:
            farm.delete()
            return Response({'message':'삭제'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':f'삭제 실패: {e}'}, status=status.HTTP_400_REQUEST)
        
class FarmReadView(APIView):
    def get(self, request, center=None):
        user_id = request.member.get('id')
        if center == '전국':
            farms = Farms.objects.all()
        elif center:
            farms = Farms.objects.filter(center=center)
        else:
            farms = Farms.objects.filter(user_id=user_id)
        serializer = FarmSerializer(farms,many=True)
        return Response(serializer.data)