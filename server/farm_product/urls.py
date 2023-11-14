from django.urls import path
from .views import FarmProductCreateView, FarmProductUpdateView, FarmProductDeleteView, FarmProductReadView, CenterProductReadView

urlpatterns = [
    path('create/', FarmProductCreateView.as_view()),
    path('update/', FarmProductUpdateView.as_view()),
    path('delete/<str:farm_product_id>/', FarmProductDeleteView.as_view()),
    path('read/', FarmProductReadView.as_view()),
    path('center/<str:center>/', CenterProductReadView.as_view()),
]
