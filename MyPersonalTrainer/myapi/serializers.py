from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField


class FilePostSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
