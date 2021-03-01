from ..cart import Cart
from test_plus.test import TestCase


class CartTest(TestCase):

    def test_cart_in_session(self):
        response = self.get('/')
        self.assertInContext('cart')