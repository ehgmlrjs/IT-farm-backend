from django.urls import path
from .views import *

urlpatterns = [
    path('pred/', OutputPredView.as_view()),
]
