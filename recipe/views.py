from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Recipe
from .serializers import *

from django.db.models import Q

class RecipeCreateView(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipeReadView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RecipeDetailReadView(APIView):
    def post(self, request):
        pk = request.data.get('recipe_id')
        recipes = Recipe.objects.filter(recipe_id=pk)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RecipeUpdateView(APIView):
    def post(self, request):
        pk = request.data.get('recipe_id')
        recipes = get_object_or_404(Recipe, recipe_id=pk)
        serializer = RecipeSerializer(recipes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipeDeleteView(APIView):
    def post(self, request):
        pk = request.data.get('recipe_id')
        recipes = get_object_or_404(Recipe, recipe_id=pk)
        try:
            recipes.delete()
            return Response({'message': '삭제'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '실패'}, status=status.HTTP_400_BAD_REQUEST)

class RecipeSearchView(APIView):
    def post(self, request):
        search = request.data.get('search', '')
        if search:
            search_list = Recipe.objects.filter(
                Q(subject__icontains=search) |
                Q(content__icontains=search) 
            )
        else:
            search_list = Recipe.objects.filter()
        serializer = RecipeSerializer(search_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
