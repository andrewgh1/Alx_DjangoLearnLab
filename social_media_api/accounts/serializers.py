from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

#User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self , validated_data):
        password = validated_data["password"]
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=CustomUser)
        print(token.key)
        return user

#User login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        extra_kwargs = {"password": {'write_only':True}}
        