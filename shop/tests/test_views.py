from django.db.models import QuerySet
from test_plus.test import TestCase

from shop.models import Category, Product


class HomePageTest(TestCase):

    def setUp(self):
        """
        Testing representation of products on homepage
        dummy_product1 is active
        dummy_product2 is not active and should not be shown
        """
        user = self.make_user('user')
        category = Category.objects.create(name='test', slug='test')
        self.dummy_product1 = Product.objects.create(
            category=category,
            name='test1',
            slug='test1',
            price='10',
            image='test',
            discount_price='9.99',
            description='',
            created_by=user, )
        self.dummy_product2 = Product.objects.create(
            category=category,
            name='test2',
            slug='test2',
            price='10',
            image='test',
            discount_price='9.99',
            description='',
            created_by=user,
            is_available=False,
        )

    def test_home_page_return_correct_html(self):
        response = self.get_check_200('/')
        self.assertTemplateUsed(response, 'shop/homepage.html')

    def test_context_data(self):
        self.get('shop:homepage')
        context = self.get_context('products')
        self.assertIsInstance(context, QuerySet)
        self.assertEqual(context.count(), 1)


class ProductDetailPageTest(TestCase):

    def setUp(self):
        user = self.make_user('user')
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
