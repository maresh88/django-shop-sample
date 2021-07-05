import json

from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from ..cart import Cart

from django.test import TransactionTestCase
from shop.models import Category, Product


class CartTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = User.objects.create_user('testuser')
        self.client.force_login(user=self.user)
        category = Category.objects.create(name='test', slug='test')
        self.dummy_product1 = Product.objects.create(
            category=category,
            name='test1',
            slug='test1',
            price='10',
            image='test',
            description='',
            created_by=self.user, )
        self.dummy_product2 = Product.objects.create(
            category=category,
            name='test2',
            slug='test2',
            price='9.00',
            image='test',
            description='',
            created_by=self.user,
        )

    def test_add_product_to_cart(self):
        data = {"product_id": 1}
        response = self.client.post('/cart/add/', json.dumps(data), content_type="application/json", xhr=True,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)

    def test_add_different_products_to_cart(self):
        self.test_add_product_to_cart()
        data = {"product_id": 2}
        response = self.client.post('/cart/add/', json.dumps(data), content_type="application/json", xhr=True,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['cart_total'], '19.00')


    def test_remove_one_product_item_from_cart(self):
        self.test_add_product_to_cart()
        self.test_add_product_to_cart()
        data2 = {"product_id": 1}
        response = self.client.post('/cart/remove_one_item/', json.dumps(data2), content_type="application/json",
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['cart_total'], '10.00')

    def test_remove_product_from_cart(self):
        self.test_add_product_to_cart()
        data3 = {"product_id": 1}
        response = self.client.post('/cart/remove/', json.dumps(data3), content_type="application/json",
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['total_cart_qty'], 0)
