from test_plus.test import TestCase
from ..models import Coupon
import datetime


class DummyCoupomModel(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(
            code='TEST',
            valid_from=datetime.datetime.now(),
            valid_to=datetime.datetime.now() + datetime.timedelta(days=1),
            discount=10,
            active=True
        )


class TestCouponModel(DummyCoupomModel):

    def test_coupon_model_creation(self):
        self.assertEqual(Coupon.objects.count(), 1)
        self.assertEqual(str(self.coupon), 'TEST')
