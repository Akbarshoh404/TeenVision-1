from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.models import Program

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)
    liked_programs = serializers.PrimaryKeyRelatedField(many=True, queryset=Program.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'age', 'gender', 'country', 'is_staff', 'is_superuser', 'liked_programs']

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
