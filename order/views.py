from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView

from cart.cart import Cart
from coupon.forms import CouponApplyForm
from order.forms import OrderCreateForm
from order.models import OrderItem, Order


class CheckoutFormView(LoginRequiredMixin, FormView):
    form_class = OrderCreateForm
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_coupon"] = CouponApplyForm()
        return context

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        form = self.get_form()
        if form.is_valid() and len(cart):
            order = form.save(commit=False)
            order.user = self.request.user
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            self.request.session['order_id'] = order.id
            return redirect('payment:process')
        return redirect('order:checkout')


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return super(OrderHistoryView, self).get_queryset().filter(user=self.request.user).order_by(
            '-id').prefetch_related('items', 'items__product')
