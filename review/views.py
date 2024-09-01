# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from .serializers import *
# from .models import *
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.response import Response
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
# from rest_framework.viewsets import ModelViewSet, GenericViewSet
# from rest_framework.permissions import IsAuthenticated

# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
    
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
#     def get_serializer_context(self):
#         return {"product_id": self.kwargs["product_pk"]}