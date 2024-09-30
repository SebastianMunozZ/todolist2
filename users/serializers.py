from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'email', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hashea la contraseña
        user.save()
        return user