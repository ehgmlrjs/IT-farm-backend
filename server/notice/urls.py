from django.urls import path
from .views import *
urlpatterns = [
    path('create/',NoticeCreateView.as_view()),
    path('read/', NoticeReadView.as_view()),
    path('update/', NoticeUpdateView.as_view()),
    path('delete/<int:notice_id>/', NoticeDeleteView.as_view()),
    path('search/', NoticeSearchView.as_view()),
    path('detail/<int:notice_id>/', NoticeDetailReadView.as_view()),
]