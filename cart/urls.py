from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.CartAdd.as_view(), name='add_to_cart'),
]
