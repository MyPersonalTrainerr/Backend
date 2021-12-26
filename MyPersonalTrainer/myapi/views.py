from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny  # <-- Here
from .serializers import PostSerializer, filePostSerializer
from django.core.files.storage import FileSystemStorage
from .models import file
from MyPersonalTrainer.settings import MEDIA_ROOT

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
        fileName=file_uploaded.name
        filePath=MEDIA_ROOT+'/'+fileName
        file.objects.create(path=filePath)
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
class Get_Path(APIView):
    permission_classes= ( AllowAny,)
    def get(self,request):
        #path=file.objects.get(id=2)
        path=file.objects.filter().order_by('-id')[0]
        context={'Path': path.path}
        return Response (context)
