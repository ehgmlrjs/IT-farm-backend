from django.urls import path
from .views import *
urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('read/', OrderReadView.as_view()),
    # path('pay/<int:order_id>/', OrderPayView.as_view()),
    path('delete/<int:order_id>/',OrderDeleteView.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/update/', ReviewUpdateView.as_view()),
    path('review/delete/<int:review_id>/', ReviewDeleteView.as_view()),
    path('review/read/<str:product_name>/', ReviewReadView.as_view()),
]
