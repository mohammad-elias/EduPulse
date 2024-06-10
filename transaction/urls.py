from django.urls import path
from .views import  PaymentSuccessView, PaymentFailedView,order_create_view

urlpatterns = [
    # path('create/', OrderCreateView, name='order-create'),
    path('create/', order_create_view, name='order-create'),
    path('success/', PaymentSuccessView.as_view(), name='payment-success'),
    path('failed/', PaymentFailedView.as_view(), name='payment-failed'),
]
