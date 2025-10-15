from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField()
    confirm_password=serializers.CharField()

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

    def validate(self, data):
        if data['password'] == data['confirm_password']:
            if data['username']:
                if User.objects.filter(username=data['username']).exists():
                    raise serializers.ValidationError('Username already exists')

            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError('Email already exists')

            return data

        raise serializers.ValidationError('passwords did not matching')

    def create(self, validated_data):
        User.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'])
        return validated_data





class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email']