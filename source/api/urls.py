from django.urls import path, include, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'shop/products', views.ViewAPIProductSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('drf-auth/', include('rest_framework.urls')),
    path('shop/categories/', views.ViewAPICategory.as_view()),
    path('shop/categories/<int:pk>/', views.ViewAPICategory.as_view()),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
