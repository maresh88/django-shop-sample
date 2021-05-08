from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='api_product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='api_product_detail'),
    path('cart/', views.CartDetailView.as_view(), name='api_cart'),
    path('order/create/', views.OrderCreateView.as_view(), name='api_order_create'),
]