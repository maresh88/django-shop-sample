from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('processing/', views.PaymentView.as_view(), name='process'),
    path('done/', views.PaymentDone.as_view(), name='done'),
    path('canceled/', views.PaymentCanceled.as_view(), name='canceled'),
]
