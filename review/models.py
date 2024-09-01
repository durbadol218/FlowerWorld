# from django.db import models
# from flowers.models import Flower
# # Create your models here.
# class Review(models.Model):
#     product = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name = "reviews")
#     date_created = models.DateTimeField(auto_now_add=True)
#     description = models.TextField(default="description")
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.description