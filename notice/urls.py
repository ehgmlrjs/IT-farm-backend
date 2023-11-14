from django.urls import path
from .views import *
urlpatterns = [
    path('create/',NoticeCreateView.as_view()),
    path('read/', NoticeReadView.as_view()),
    path('update/', NoticeUpdateView.as_view()),
    path('delete/', NoticeDeleteView.as_view()),
    path('search/', NoticeSearchView.as_view()),
    path('detail/', NoticeDetailReadView.as_view()),
]