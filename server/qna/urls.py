from django.urls import path
from .views import *
urlpatterns = [
    path('create/', QnaCreateView.as_view()),
    path('read/',QnaReadView.as_view()),
    path('detail/', QnaDetailReadView.as_view()),
    path('update/', QnaUpdateView.as_view()),
    path('delete/',QnaDeleteView.as_view()),
    path('search/', QnaSearchView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/read/', CommentReadView.as_view()),
    path('comment/update/', CommentUpdateView.as_view()),
    path('comment/delete/', CommentDeleteView.as_view()),
]