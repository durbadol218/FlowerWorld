from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FlowerCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Flower(models.Model):
    seller = models.ForeignKey(User, related_name="flower_seller", on_delete=models.CASCADE)
    flower_name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers/images/')
    category = models.ManyToManyField(FlowerCategory, related_name='flowers',)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.flower_name


