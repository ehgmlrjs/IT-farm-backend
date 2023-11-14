from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductReadView, ProductSearchView, ProductDetailReadView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('update/', ProductUpdateView.as_view()),
    path('delete/<int:product_id>/', ProductDeleteView.as_view()),
    path('read/', ProductReadView.as_view()),
    path('search/<str:product_name>/', ProductSearchView.as_view()),
    path('detail/<int:product_id>/', ProductDetailReadView.as_view()),
]
