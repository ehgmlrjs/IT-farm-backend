from django.urls import path
from .views import *
urlpatterns = [
    path('create/', QnaCreateView.as_view()),
    path('read/',QnaReadView.as_view()),
    path('detail/<int:qna_id>/', QnaDetailReadView.as_view()),
    path('update/', QnaUpdateView.as_view()),
    path('delete/<int:qna_id>/',QnaDeleteView.as_view()),
    path('search/', QnaSearchView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/read/<int:qna>/', CommentReadView.as_view()),
    path('comment/update/', CommentUpdateView.as_view()),
    path('comment/delete/<int:comment_id>/', CommentDeleteView.as_view()),
]