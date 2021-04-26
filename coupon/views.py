from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Coupon
from .forms import CouponApplyForm


class CouponApply(TemplateView):
    template_name = 'order/checkout.html'

    def post(self, request, *args, **kwargs):
        now = timezone.now()
        form = CouponApplyForm(self.request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                self.request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                self.request.session['coupon_id'] = None
        return redirect('order:checkout')
