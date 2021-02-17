from test_plus.test import TestCase
from django.urls import reverse
from shop.models import Category, Product
from .test_models import DummyGenerator


class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        response = self.get_check_200('/')
        self.assertTemplateUsed(response, 'shop/homepage.html')


class ProductDetailPageTest(TestCase):

    def setUp(self):
        user = DummyGenerator()
        user = user.dummy_user()
        category = Category.objects.create(name='test', slug='test')
        self.dummy_product = Product.objects.create(
            category=category,
            name='test',
            slug='test',
            price='10',
            image='test',
            discount_price='9.99',
            description='',
            created_by=user,
        )

    def test_product_detail_url(self):
        url = self.reverse('shop:product_detail', pk='1', slug='test')
        response = self.get_check_200(url)
        self.assertTemplateUsed(response, 'shop/product_detail.html')


class CategoryPageTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='test', slug='test')

    def test_category_url(self):
        url = self.reverse('shop:products_by_category', category_slug='test')
        response = self.get_check_200(url)
        self.assertTemplateUsed(response, 'shop/product_list.html')