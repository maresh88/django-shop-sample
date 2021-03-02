from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import JsonResponse
from .cart import Cart
from shop.models import Product


class CartAdd(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        return JsonResponse({'added': 'OK'})
