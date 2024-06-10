from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, Transaction
from features.models import Plan
from .serializers import OrderSerializer, TransactionSerializer
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, permission_classes
# @method_decorator(csrf_exempt)
# @csrf_exempt
# class OrderCreateView(generics.CreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         user = request.user
#         plan_id = request.data.get('plan_id')

#         if not plan_id:
#             return Response({"error": "Plan ID is required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             plan = Plan.objects.get(id=plan_id)
#         except Plan.DoesNotExist:
#             return Response({"error": "Invalid Plan ID"}, status=status.HTTP_404_NOT_FOUND)

#         # Create the order
#         order = Order.objects.create(user=user, plan=plan)
        
#         # Redirect to SSLCommerz payment gateway
#         payment_url = sslcommerz_payment_gateway(request, order.id, user.id, plan.price)
#         return redirect(payment_url)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_create_view(request):
    user = request.user
    plan_id = request.data.get('plan_id')

    if not plan_id:
        return Response({"error": "Plan ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        plan = Plan.objects.get(id=plan_id)
    except Plan.DoesNotExist:
        return Response({"error": "Invalid Plan ID"}, status=status.HTTP_404_NOT_FOUND)

    # Create the order
    order = Order.objects.create(user=user, plan=plan)
    
    # Redirect to SSLCommerz payment gateway
    payment_url = sslcommerz_payment_gateway(request, order.id, user.id, plan.price)
    return redirect(payment_url)


# @method_decorator(csrf_exempt)
# @csrf_exempt
class PaymentSuccessView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        tran_id = request.GET.get('tran_id')
        order_id = request.GET.get('value_a')
        
        order = get_object_or_404(Order, id=order_id)
        
        # Create the transaction record
        Transaction.objects.create(order=order, amount=order.plan.price, status='Success')
        
        # Update user plan
        user = order.user
        user.plan = order.plan
        user.save()

        return Response({"message": "Payment successful and plan updated."}, status=status.HTTP_200_OK)


# @method_decorator(csrf_exempt, name='dispatch')
# @csrf_exempt
class PaymentFailedView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"error": "Payment failed or canceled."}, status=status.HTTP_400_BAD_REQUEST)

# Ensure you have the necessary URL paths configured in your urls.py
