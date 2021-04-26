import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # allauth
    path('accounts/', include('allauth.urls')),

    # apps
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupon/', include('coupon.urls', namespace='coupon')),
    path('', include('shop.urls', namespace='shop')),

    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
