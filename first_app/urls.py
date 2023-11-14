from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include('users.urls')),
    path("farms/", include('farms.urls')),
    path("farm_product/", include('farm_product.urls')),
    path("product/", include('product.urls')),
    path('notice/', include('notice.urls')),
    path('qna/', include('qna.urls')),
    path('event/', include('event.urls')),
    path('recipe/', include('recipe.urls')),
    path("pest/", include('pest.urls')),
    path('order/', include('order.urls')),
    path("cart/", include('cart.urls')),
]
