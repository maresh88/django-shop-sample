import decimal
from decimal import Decimal
from config.tests.test_logged_user import LoggedUser
from shop.tests.test_models import TestProductModel
from order.models import Order, OrderItem


class DummyOrderAndOrderItemModels(TestProductModel):

    def setUp(self):
        super(DummyOrderAndOrderItemModels, self).setUp()
        self.order = Order.objects.create(
            user=self.user,
            address='Stroiteley 1',
            postal_code='123456',
            city='Moscow',
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.dummy_product,
            price=self.dummy_product.price,
        )


class TestOrderAndOrderItemModels(DummyOrderAndOrderItemModels):
    def test_order_model_creation(self):
        self.assertEqual(str(self.order), f'Order {self.order.id}')

    def test_order_item_model_creation(self):
        self.assertEqual(str(self.order_item), '1')

    def test_order_total_cost(self):
        self.order.discount = 10
        self.assertEqual(self.order.get_total_cost(), Decimal('9.00'))

    def test_order_item_get_cost(self):
        self.assertEqual(self.order_item.get_cost(), '10')
