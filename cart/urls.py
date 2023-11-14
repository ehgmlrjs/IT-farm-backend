from django.urls import path
from .views import CartCreateView, CartUpdateView, CartDeleteView, CartReadView

urlpatterns = [
    path('create/', CartCreateView.as_view()),
    path('update/', CartUpdateView.as_view()),
    path('delete/<int:cart_id>/', CartDeleteView.as_view()),
    path('read/', CartReadView.as_view()),
]