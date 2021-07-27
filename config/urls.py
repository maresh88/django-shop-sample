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



    # rest framework
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('shop.api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # debug toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
