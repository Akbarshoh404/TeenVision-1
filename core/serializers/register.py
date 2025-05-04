from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
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
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        first_name, last_name = full_name.split(" ", 1)

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validators(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise AuthenticationFailed("Foydalanuvchi ro'yxatdan o'tmagan!")

        # Agar hammasi yaxshi bo‘lsa, foydalanuvchini qaytaramiz
        attrs['user'] = user
        return attrs
