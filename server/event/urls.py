from django.urls import path
from .views import *
urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('read/',EventReadView.as_view()),                                                                                                                                                                                                                            
]
