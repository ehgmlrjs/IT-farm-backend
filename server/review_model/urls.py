from django.urls import path
from .views import *

urlpatterns = [
    path('pred/', ReviewPredView.as_view()),
]
