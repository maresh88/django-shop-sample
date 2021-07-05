from config.tests.test_logged_user import LoggedUser
from cart.tests.test_views import CartTest


class TestOrderViewWithEmptyCart(LoggedUser):
    def test_create_order_GET(self):
        response = self.client.get('/order/checkout/')
        self.assertTemplateUsed(response, 'order/checkout.html')

    def test_create_order_with_empty_cart_POST(self):
        response = self.client.post('/order/checkout/')
        self.assertRedirects(response, '/order/checkout/')


class TestOrderViewWithFilledCart(CartTest):
    def test_create_order_POST(self):
        self.test_add_product_to_cart()
        response = self.client.post('/order/checkout/', data={
            'city': 'Moscow',
            'address': 'Stroiteley 1',
            'address_optional': '',
            'postal_code': '123456'
        })
        self.assertRedirects(response, '/payment/processing/')
