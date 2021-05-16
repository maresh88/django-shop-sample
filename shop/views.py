from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf import settings

from .models import Category, Product

r = settings.R


class AvailabilityMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_available=True)


class HomePageView(AvailabilityMixin, ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/homepage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(AvailabilityMixin, DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_product_purchases'] = r.get(
            f'product:{self.get_object().id}:num_of_purchases')
        return context


class ProductsByCategory(HomePageView):
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        return super(ProductsByCategory, self).get_queryset().filter(category__slug=self.kwargs.get('category_slug'))
