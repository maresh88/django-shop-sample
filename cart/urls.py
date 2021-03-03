from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.CartAdd.as_view(), name='add_to_cart'),
    path('detail/', views.CartDetail.as_view(), name='cart_detail'),
]
