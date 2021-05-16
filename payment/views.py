import braintree
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from config import settings
from order.models import Order
from order.tasks import send_mail_with_order

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

r = settings.R


class PaymentView(View):
    order = None

    def dispatch(self, request, *args, **kwargs):
        order_id = self.request.session.get('order_id')
        self.order = get_object_or_404(Order, id=order_id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        client_token = gateway.client_token.generate()
        return render(request, 'payment/process.html', {'order': self.order,
                                                        'client_token': client_token})

    def post(self, request, *args, **kwargs):
        total_cost = self.order.get_total_cost()
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            product_ids = self.order.items.values_list('product_id', flat=True)
            for product_id in product_ids:
                r.incr(f'product:{product_id}:num_of_purchases')
            self.order.paid = True
            self.order.braintree_id = result.transaction.id
            self.order.save()

            # sending email
            if self.order.user.email:
                send_mail_with_order.delay(self.order.id)

            if request.session.get('coupon_id'):
                del request.session['coupon_id']
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')


class PaymentDone(TemplateView):
    template_name = 'payment/done.html'


class PaymentCanceled(TemplateView):
    template_name = 'payment/canceled.html'
