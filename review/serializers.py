# from rest_framework import serializers
# from . models import Review

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ["id", "date_created", "name", "description"]
    
#     def create(self, validated_data):
#         product_id = self.context["id"]
#         return Review.objects.create(product_id = product_id,  **validated_data)