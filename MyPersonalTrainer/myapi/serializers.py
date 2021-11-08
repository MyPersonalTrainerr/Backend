from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny  # <-- Here
from .serializers import PostSerializer


class signUpApi(generics.GenericAPIView):
    permission_classes= ( AllowAny,)
    serializer_class=PostSerializer
    def post(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)