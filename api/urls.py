from django.urls import path

from api.views.generics import (
    ProductListAPIView, 
    ProductDetailAPIView, 
    CategoryListAPIView, 
    CategoryDetailAPIView
)

urlpatterns = [
  
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),

  
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
]