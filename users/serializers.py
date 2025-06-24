from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}  # hide password in GET
        }

    def create(self, validated_data):
        # Hash the password here if needed
        user = UserModel(**validated_data)
        # You can use something like Django's make_password here
        user.save()
        return user
