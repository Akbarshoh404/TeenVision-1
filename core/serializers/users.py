from django.contrib.auth import get_user_model
from rest_framework import serializers
from django_countries.fields import CountryField as CountrySerializerField

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    liked_programs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    country = CountrySerializerField(default='UZ')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'gender', 'country', 'liked_programs']


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
