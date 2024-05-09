from rest_framework import serializers
from .models import User
from rest_framework.response import Response


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'status', 'created_at']

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.save()
        return user

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({
                'phone_number': 'Phone number already exists.'
            })
        return attrs


