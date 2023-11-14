from django.urls import path
from .views import *
urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('read/', OrderReadView.as_view()),
    path('pay/', OrderPayView.as_view()),
    path('delete/',OrderDeleteView.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/update/', ReviewUpdateView.as_view()),
    path('review/delete/', ReviewDeleteView.as_view()),
    path('review/read/', ReviewReadView.as_view()),
]
