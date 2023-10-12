from django.urls import path, include

from . import views


urlpatterns = [
    path('shop/products/', views.ViewAPIProduct.as_view({'get': 'list', 'post': 'create'})),
    path('shop/products/<int:pk>/', views.ViewAPIProduct.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('shop/categories/', views.ViewAPICategory.as_view()),
    path('shop/categories/<int:pk>/', views.ViewAPICategory.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
