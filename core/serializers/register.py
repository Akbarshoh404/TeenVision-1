from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    full_name = serializers.CharField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']

    def validate_full_name(self, value):
        # Full name kamida 2 ta so'zdan iborat bo'lishi kerak
        if len(value.split()) < 2:
            raise serializers.ValidationError("Iltimos, to'liq ismingizni kiriting (ism va familiya).")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email ro'yxatdan o'tkazilgan. Iltimos, boshqa email kiriting.")
        return value

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        first_name, last_name = full_name.split(" ", 1)

        password = validated_data.pop('password')

        user = User(
            first_name=first_name,
            last_name=last_name,
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email va parol kiriting!")

        user = authenticate(username=email, password=password)

        if not user:
            raise AuthenticationFailed("Email yoki parol noto'g'ri!")

        # Agar hammasi yaxshi bo‘lsa, foydalanuvchini qaytaramiz
        data['user'] = user
        return data


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'age', 'gender', 'country']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'age': {'required': False},
            'gender': {'required': False},
            'country': {'required': False}
        }
