from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import ProductSerializer, OrderSerializer
from shop.models import Product
from order.models import OrderItem, Order
from cart.cart import Cart


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer


class CartDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        cart = request.session.get('cart')
        return Response(cart)


class OrderCreateView(CreateAPIView):
    cart = None
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        self.cart = Cart(request)
        if self.cart:
            return self.create(request, *args, **kwargs)
        else:
            return Response(status=403)

    def perform_create(self, serializer):
        obj = serializer.save(user=self.request.user)
        for item in self.cart:
            OrderItem.objects.create(order=obj,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])




