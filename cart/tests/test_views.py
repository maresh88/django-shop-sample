import json

from django.urls import reverse, reverse_lazy

from ..cart import Cart

from test_plus.test import TestCase
from shop.models import Category, Product


class CartTest(TestCase):
    def setUp(self):
        user = self.make_user('user')
        category = Category.objects.create(name='test', slug='test')
        self.dummy_product1 = Product.objects.create(
            category=category,
            name='test1',
            slug='test1',
            price='10',
            image='test',
            description='',
            created_by=user, )
        self.dummy_product2 = Product.objects.create(
            category=category,
            name='test2',
            slug='test2',
            price='9.00',
            image='test',
            description='',
            created_by=user,
        )

    def test_cart_in_session(self):  # TODO finishing the cart test
        response = self.get('/')
        self.assertInContext('cart')
