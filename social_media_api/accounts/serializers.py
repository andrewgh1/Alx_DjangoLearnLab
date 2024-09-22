from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token


User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

#User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    

    def create(self , validated_data):
        password = validated_data["password"]
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=User)
        print(token.key)
        return user

#User login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
