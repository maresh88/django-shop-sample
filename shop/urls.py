from django.contrib import admin
from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('category/<slug:category_slug>/', views.ProductsByCategory.as_view(), name='products_by_category'),
    path('detail/<int:pk>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('', views.HomePageView.as_view(), name='homepage'),
]
