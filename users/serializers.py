from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Image

User = get_user_model()


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['profile'] = ProfileSerializer(user.image).data
        return token


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'access']

    def create(self, validated_data):
        # username = validated_data['username']
        password = validated_data['password']
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        token_custom = CustomTokenSerializer().get_token(new_user)
        validated_data['access'] = str(token_custom.access_token)
        return validated_data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    profile = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
            print(user.username)
        except User.DoesNotExist:
            raise serializers.ValidationError('not a valid username')

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect credentials')
        print(user.image)
        dana = {
            **data,
            "profile": ProfileSerializer(user.image).data
        }
        custom_token = CustomTokenSerializer.get_token(user)

        data['access'] = str(custom_token.access_token)
        data['profile'] = ProfileSerializer(user.image).data
        return data
