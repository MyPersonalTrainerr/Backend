from rest_framework import serializers
from django.contrib.auth.models import User
from .models import file

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'email','username','password',
        )
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class filePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=file
        fields=('path',)
    def create(self,validated_data):
        File=file(
            path=validated_data['path']
        )
        File.save()
        return File
