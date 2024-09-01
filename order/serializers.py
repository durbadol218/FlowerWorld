from rest_framework import serializers
from .models import Order, OrderItem
from flowers.models import Flower
from flowers.serializers import FlowerSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    flower = FlowerSerializer()  

    class Meta:
        model = OrderItem
        fields = ["id", "flower", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'placed_time', 'status', 'user', 'items']

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ["id", "created_at", "updated_at",]






















# class OrderItemSerializer(serializers.Serializer):
#     class Meta:
#         model = OrderItem
#         fields = ['id','flower', 'quantity']
# class OrderSerializer(serializers.Serializer):
#     items = OrderItemSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ['id','placed_at','status', 'user','items']
    
#     def create(self, validated_data):
#         items_data = validated_data.pop('items')
#         order = Order.objects.create(**validated_data)
#         for item_data in items_data:
#             OrderItem.objects.create(order=order, **item_data)
#         return order

# class OrderSerializer(serializers.ModelSerializer):
#     floer = FlowerSerializer()
#     class Meta:
#         model = Order
#         # fields = ('user',) 
#         fields = ['id', 'user', 'flower', 'status', 'quantity', 'total_amount','created_at', 'updated_at']