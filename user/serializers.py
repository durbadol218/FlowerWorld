from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from .constants import USER_TYPE


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'account']
        
class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.Account
        fields = ['user', 'user_type', 'phone', 'image']
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE, required=True)
    image = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'user_type', 'phone', 'image']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        user_type = self.validated_data['user_type']
        phone = self.validated_data['phone']
        image = self.validated_data.get('image')
        
        if password != password2:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already Exists"})
        
        
        user = User(username=username, email=email,first_name=first_name,last_name=last_name)
        print(user)
        user.set_password(password)
        user.is_active = False
        user.save()
        
        account = models.Account.objects.create(user=user, user_type=user_type)
        account.save()
        return user

# class AccountRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Account
#         fields = ['user','image', 'phone', 'user_type']

#     def save(self):
#         user = self.validated_data['user']
#         phone = self.validated_data['phone']
#         image = self.validated_data['image']
#         user_type = self.validated_data['user_type']
#         account = models.Account(user=user, phone=phone, image=image, user_type=user_type)
#         account.save()
#         return account
    


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)