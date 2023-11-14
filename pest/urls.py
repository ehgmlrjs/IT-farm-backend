from django.urls import path
from .views import PestCreateView, PestUpdateView, PestDeleteView, PestReadView, PestSolutionView

urlpatterns = [
    path('create/', PestCreateView.as_view()),
    path('update/', PestUpdateView.as_view()),
    path('delete/<int:pest_id>/', PestDeleteView.as_view()),
    path('read/<int:farm_id>/', PestReadView.as_view()),
    path('solution/', PestSolutionView.as_view()),
]
