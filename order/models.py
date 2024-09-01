from django.db import models
from django.contrib.auth.models import User
from flowers.models import Flower

# class Cart(models.Model):
#     cart_id = models.CharField(max_length=50, unique=True, editable=False,primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return str(self.cart_id)

# class Cartitems(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
#     flower = models.ForeignKey(Flower, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
#     quantity = models.PositiveSmallIntegerField(default=0)

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    placed_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="Pending")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.flower.flower_name
