# from django.urls import path
# from . import views
# from .views import FlowerListAPIView, FlowerListByCategoryView

# urlpatterns = [
#     path('flowers/', views.FlowerListAPIView.as_view(), name='flower-list'),
#     path('categories/', views.CategoryListView.as_view(), name='category-list'),
#     path('flowers/category/<int:category_id>/', FlowerListByCategoryView.as_view(), name='flowers-by-category'),
#     # # path('flowers/buy/<int:pk>/', BuyFlowerAPIView.as_view(), name='buy-flower'),
#     path('flowers/<int:pk>/', views.FlowerDetailView.as_view(), name='flower-detail'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'flowers', FlowerViewSet, basename='flower')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
