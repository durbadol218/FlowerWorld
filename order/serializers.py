from rest_framework import serializers
from .models import Order
from flowers.models import Flower

class OrderSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    flower_name = serializers.SerializerMethodField()
    flower_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id','user','username', 'placed_time', 'status', 'flower', 'flower_name', 'flower_price', 'quantity', 'total_amount']
    
    def get_username(self, obj):
        return obj.user.user.username if obj.user and obj.user.user else None
    
    def get_flower_name(self, obj):
        return obj.flower.flower_name if obj.flower else None
    
    def get_flower_price(self, obj):
        return obj.flower.price if obj.flower else None
