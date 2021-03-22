import json
from decimal import Decimal

from django.shortcuts import get_object_or_404
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from .cart import Cart
from shop.models import Product


class CartAdd(View):
    def post(self, request):
        body_data = json.loads(request.body.decode('utf-8'))
        print(body_data)
        cart = Cart(request)
        product = get_object_or_404(Product, id=body_data.get('product_id'))
        cart.add(product=product)
        product_subtotal = cart.cart[str(product.id)]['quantity'] * Decimal(cart.cart[str(product.id)]['price'])
        return JsonResponse({
            'total_cart_qty': cart.__len__(),
            'subtotal': product_subtotal,
            'cart_total': cart.get_total_price()
        })


class CartDetail(TemplateView):
    template_name = 'cart/cart_detail.html'


class CartRemoveOneItem(View):
    def post(self, request):
        body_data = json.loads(request.body.decode('utf-8'))
        cart = Cart(request)
        product = get_object_or_404(Product, id=body_data.get('product_id'))
        cart.remove_one_item(product)
        product_subtotal = cart.cart[str(product.id)]['quantity'] * Decimal(cart.cart[str(product.id)]['price'])
        return JsonResponse({
            'total_cart_qty': cart.__len__(),
            'cart_total': cart.get_total_price(),
            'subtotal': product_subtotal,
        })


class CartRemove(View):
    def post(self, request):
        body_data = json.loads(request.body.decode('utf-8'))
        cart = Cart(request)
        product = get_object_or_404(Product, id=body_data.get('product_id'))
        cart.remove(product)
        return JsonResponse({
            'total_cart_qty': cart.__len__(),
            'cart_total': cart.get_total_price()
        })
