from django.urls import path
from .views import *

urlpatterns = [
    path('create/', RecipeCreateView.as_view()),
    path('read/', RecipeReadView.as_view()),
    path('detail/',RecipeDetailReadView.as_view()),
    path('update/', RecipeUpdateView.as_view()),
    path('delete/', RecipeDeleteView.as_view()),
    path('search/', RecipeSearchView.as_view()),
]
