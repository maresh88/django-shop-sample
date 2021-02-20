from django.contrib.auth.models import User
from test_plus.test import TestCase

from shop.models import Category, Product


class DummyGenerator(TestCase):

    def dummy_user(self):
        user = User.objects.create(username='dummy')
        user.set_password('123456789')
        user.save()
        return user


class TestCategoryModel(TestCase):

    def setUp(self):
        self.dummy_category = Category.objects.create(name='test', slug='test')

    def test_category_model_creation(self):
        data = self.dummy_category
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'test')


class TestProductModel(TestCase):

    def setUp(self):
        user = DummyGenerator()
        user = user.dummy_user()
        category = Category.objects.create(name='test', slug='test')
        self.dummy_product = Product.objects.create(
            category=category,
            name='test',
            slug='test',
            price='10',
            discount_price='9.99',
            description='',
            created_by=user,
        )

    def test_product_model_creation(self):
        data = self.dummy_product
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'test')
