import re

from rest_framework import serializers

from shop.models import Product
from order.models import OrderItem, Order
from coupon.models import Coupon


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'category', 'name',
                  'price', 'discount_price',
                  'description', 'label')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem


class OrderSerializer(serializers.ModelSerializer):
    coupon = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ('address', 'address_optional', 'postal_code', 'city',
                  'coupon',)

    def validate_postal_code(self, value):
        if not re.match(r'^[1-9]\d{5}$', str(value)):
            raise serializers.ValidationError('Please provide a valid postal code')
        return str(value)
