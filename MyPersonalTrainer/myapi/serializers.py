from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer,FileField

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

class filePostSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']