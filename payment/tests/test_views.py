from config.tests.test_logged_user import LoggedUser
from order.tests.test_models import DummyOrderAndOrderItemModels
from order.models import Order


class TestPaymentViews(DummyOrderAndOrderItemModels):

    def test_payment_view_GET(self):
        self.client.session['order_id'] = self.order.id
        print(self.client.session['order_id'])
        print(Order.objects.all())
        url = self.reverse('payment:process')
        response = self.client.get('/payment/processing/')
        print(response)

        self.assertTemplateUsed(response, 'payment/process.html')
