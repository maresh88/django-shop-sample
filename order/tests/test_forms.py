from order.forms import OrderCreateForm
from test_plus.test import TestCase

class OrderFormAddressTest(TestCase):
    def test_checkout_form_raise_address_error(self):
        form = OrderCreateForm(data={
            'city': 'Moscow',
            'address': 'No Digits',
            'address_optional': '',
            'postal_code': '111111'
        })
        self.assertFalse(form.is_valid())

    def test_checkout_form_raise_postal_code_error(self):
        form = OrderCreateForm(data={
            'city': 'Moscow',
            'address': 'Stroiteley 1',
            'address_optional': '',
            'postal_code': '012345'
        })
        self.assertFalse(form.is_valid())