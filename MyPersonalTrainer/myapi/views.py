from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny  # <-- Here
from .serializers import PostSerializer, filePostSerializer
from django.core.files.storage import FileSystemStorage

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class signUpApi(generics.GenericAPIView):
    permission_classes= ( AllowAny,)
    serializer_class=PostSerializer
    def post(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
class fileUploadApi(APIView):
    permission_classes= ( AllowAny,)
    serializer_class=filePostSerializer
    def get(self, request):
        return Response("GET API")
    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        fs = FileSystemStorage()
        fs.save(file_uploaded.name,file_uploaded)
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)