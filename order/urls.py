from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]












# flower_router = routers.NestedDefaultRouter({router, 'flower', lo})
# flower_router.register('reviews', views.ReviewViewSet, basename="products_review")


# router = routers.DefaultRouter()
# router.register('orders', views.OrderViewSet)



# urlpatterns = [
#     path('add-order/<str:id>/<str:token>/', views.add_order, name='add-order'),
#     path('', include(router.urls)),
# ]
# urlpatterns = [
#     # path('add-order/<str:id>/<str:token>/', views.add_order, name='add-order'),
#     path('', include(router.urls)),
# ]