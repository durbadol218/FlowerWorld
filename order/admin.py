# from django.contrib import admin
# from . import models
# # Register your models here.
# admin.site.register(models.Order)
# admin.site.register(models.OrderItem)


# from django.contrib import admin
# from .models import Order
# from flowers.models import Flower

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'name', 'email', 'phone', 'flower', 'status', 'cancel', 'placed_at')
#     list_filter = ('status', 'cancel', 'placed_time')
#     search_fields = ('name', 'email', 'phone', 'address', 'flower__flower_name')
#     ordering = ('-created_at',)
    
#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('flower')

# admin.site.register(Order, OrderAdmin)


from django.contrib import admin
from .models import Order
from flowers.models import Flower

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'placed_time', 'status', 'flower', 'quantity', 'total_amount')
    list_filter = ('status', 'placed_time')
    search_fields = ('user__username', 'flower__flower_name')

admin.site.register(Order, OrderAdmin)