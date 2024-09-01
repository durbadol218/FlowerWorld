# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Flower, FlowerCategory
# from . import serializers
# from .serializers import FlowerSerializer, FlowerCategorySerializer
# from django.shortcuts import get_object_or_404

# class FlowerListAPIView(generics.ListAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         category_id = self.request.query_params.get('category_id')
#         print(category_id)
#         if category_id:
#             queryset = queryset.filter(id=category_id)
#         return queryset

# class FlowerListByCategoryView(generics.ListAPIView):
#     serializer_class = FlowerSerializer

#     def get_queryset(self):
#         category_id = self.kwargs['category_id']
#         return Flower.objects.filter(category_id=category_id)


# class FlowerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer

# class CategoryListView(generics.ListCreateAPIView):
#     queryset = FlowerCategory.objects.all()
#     serializer_class = serializers.FlowerCategorySerializer
    
# class BuyFlowerAPIView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = FlowerSerializer

#     def post(self, request, pk):
#         flower = get_object_or_404(Flower, pk=pk)

#         if flower.stock > 0:
#             flower.stock -= 1
#             flower.save()
#             # Here you would also create an Order instance and send an email
#             return Response({'message': 'Flower purchased successfully!'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'This flower is out of stock!'}, status=status.HTTP_400_BAD_REQUEST)




from rest_framework import viewsets
from .models import Flower, FlowerCategory
from .serializers import FlowerSerializer, FlowerCategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>\d+)')
    def list_by_category(self, request, category_id=None):
        queryset = Flower.objects.filter(category_id=category_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = FlowerCategory.objects.all()
    serializer_class = FlowerCategorySerializer