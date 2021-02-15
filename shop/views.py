from django.views.generic.list import ListView
from .models import Product


class AvailabilityMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_available=True)


class HomePageView(AvailabilityMixin, ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
