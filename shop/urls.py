from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('detail/<int:pk>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
