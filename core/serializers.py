from rest_framework import serializers
from .models import UserModel



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        #fields = "__all__"
        exclude = ["id", "user_permissions", "groups", "is_staff", "is_active", "otp_enabled", "otp_verified", "otp_base32", "otp_auth_url", "last_login"]
        extra_kwargs = {'password': {'write_only': True}}  # Adicione esta linha se quiser que a senha seja write_only
              

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CustomUserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["use_permission"]
        
        
