from rest_framework import serializers
from django.contrib.auth.models import User
from .models import HeartUser, Profile, RestTest

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('age',)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class HeartUserSerializer(serializers.ModelSerializer):
    heartuser = UserSerializer()
    profile = ProfileSerializer()

    def create(self, validated_data):
        return HeartUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        pass

    class Meta:
        model = HeartUser
        fields = '__all__'

class RestTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestTest
        fields = "__all__"

    def create(self, validated_data):
        return RestTest.objects.create(**validated_data)