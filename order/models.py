from django.db import models
from user.models import Account
from flowers.models import Flower

class Order(models.Model):
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Cancelled', 'Cancelled'),
        ('Failed', 'Failed'),
    ]
    user = models.ForeignKey(Account,on_delete=models.CASCADE,blank=True,null=True)
    placed_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default="Pending")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.PositiveSmallIntegerField(default=0, null=True)
    total_amount = models.FloatField(verbose_name='Total amount of order', default=0)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-placed_time']