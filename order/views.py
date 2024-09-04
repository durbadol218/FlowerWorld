from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from flowers.models import Flower

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            queryset = queryset.filter(user_id=customer_id)
        return queryset

    def perform_create(self, serializer):
        flower = serializer.validated_data.get('flower')
        user_account = serializer.validated_data.get('user')
        quantity = serializer.validated_data.get('quantity')

        if user_account:
            email = user_account.user.email  # Retrieve email from related User model
        else:
            email = None

        if flower and flower.stock >= quantity:
            # Update flower stock
            flower.stock -= quantity
            flower.save()

            # Calculate total amount
            total_amount = flower.price * quantity

            # Save order with total amount
            order = serializer.save(total_amount=total_amount)

            # Send confirmation email
            if email:
                email_subject = "Thank You for Your Order"
                email_body = render_to_string('orderemail.html', {
                    'flower_name': flower.flower_name,
                    'quantity': quantity,
                    'total_amount': total_amount,
                    'email': email,
                    'phone': user_account.phone  # Use phone from Account model
                })
                email_message = EmailMultiAlternatives(email_subject, '', to=[email])
                email_message.attach_alternative(email_body, "text/html")
                email_message.send()
        else:
            # Handle case where flower is out of stock or quantity is invalid
            raise serializers.ValidationError("Insufficient stock for the selected flower.")

        
class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Order, pk=pk)

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






