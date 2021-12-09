from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny  # <-- Here
from .serializers import PostSerializer, filePostSerializer

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
class fileUploadApi(generics.GenericAPIView):
    permission_classes= ( AllowAny,)
    serializer_class=filePostSerializer
    def post(self,request,*args,**kwargs):
        serializer2=filePostSerializer(data=request.data)
        serializer2.is_valid()
        serializer2.save()
        return Response(serializer2.data)