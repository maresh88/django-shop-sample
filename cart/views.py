from django.shortcuts import get_object_or_404
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from .cart import Cart
from shop.models import Product


class CartAdd(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        return JsonResponse({'total_cart_qty': cart.__len__()})


class CartDetail(TemplateView):
    template_name = 'cart/cart_detail.html'


class CartRemoveOneItem(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove_one_item(product)
        return JsonResponse({
            'total_cart_qty': cart.__len__(),
            })


class CartRemove(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return JsonResponse({'total_cart_qty': cart.__len__()})