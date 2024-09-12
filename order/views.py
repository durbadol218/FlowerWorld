from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from flowers.models import Flower
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#Previous versions
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete', 'head', 'options']
    
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
        
        print(f"Flower: {flower}")
        print(f"User Account: {user_account}")
        print(f"Quantity: {quantity}")


        email=None
        if user_account:
            email = user_account.user.email
            print(f"User email: {email}")
            
        if flower and flower.stock >= quantity:
            flower.stock -= quantity
            flower.save()
            total_amount = flower.price * quantity

            order = serializer.save(total_amount=total_amount)

            if email:
                print("Email:", email)
                email_subject = "Thank You for Your Order"
                email_body = render_to_string('orderemail.html', {
                    'flower_name': flower.flower_name,
                    'quantity': quantity,
                    'total_amount': total_amount,
                    'email': email,
                    'phone': user_account.phone
                })
                print(f"Email Subject: {email_subject}")
                print(f"Email Body: {email_body}")
                try:
                    email_message = EmailMultiAlternatives(email_subject, '', to=[email])
                    email_message.attach_alternative(email_body, "text/html")
                    email_message.send()
                    print(f"Email sent to {email}")
                except Exception as e:
                    print(f"Failed to send email: {e}")
            else:
                print("No email found!")
        else:
            raise serializers.ValidationError("Insufficient stock for the selected flower.")
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        status_before_update = instance.status

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if serializer.validated_data.get('status') == 'Completed' and status_before_update != 'Completed':
            user_email = instance.user.email
            if user_email:
                email_subject = "Order Completed"
                email_body = render_to_string('order_completed_email.html', {
                    'user': instance.user,
                    'order': instance,
                })
                email_message = EmailMultiAlternatives(email_subject, '', to=[user_email])
                email_message.attach_alternative(email_body, "text/html")
                email_message.send()
        return Response(serializer.data)


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






