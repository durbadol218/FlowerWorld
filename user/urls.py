# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views

# router = DefaultRouter()

# router.register('list',views.AccountViewset)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', views.UserRegistrationApiView.as_view(), name="register"),
#     path('register_account/', views.AccountRegistrationApiView.as_view(), name="register_account"),
#     path('login/', views.UserLoginApiView.as_view(), name="login"),
#     path('logout/', views.UserLogoutApiView.as_view(), name="logout"),
#     path('activate/<uid64>/<token>/' , views.activateAccount, name="activate"),
    
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewset, UserRegistrationApiView, AccountRegistrationApiView, activateAccount, UserLoginApiView, UserLogoutApiView

router = DefaultRouter()
router.register(r'accounts', AccountViewset, basename='account')

urlpatterns = [
    path('api/', include(router.urls)),
    path('user/register/', UserRegistrationApiView.as_view(), name='register'),
    path('account/register/', AccountRegistrationApiView.as_view(), name='account_register'),
    path('user/activate/<uid64>/<token>/', activateAccount, name='activate'),
    path('user/login/', UserLoginApiView.as_view(), name='login'),
    path('user/logout/', UserLogoutApiView.as_view(), name='logout'),
]