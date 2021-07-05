from .test_model import DummyCoupomModel


class TestCouponView(DummyCoupomModel):
    def test_coupon_is_valid(self):
        response = self.post('coupon:apply', data={'code': 'TEST'})
        self.assertEqual(response.status_code, 302)

    def test_coupon_invalid_input(self):
        self.post('coupon:apply', data={'code': 'invalid_code'})
        self.assertIsNone(self.client.session['coupon_id'])
