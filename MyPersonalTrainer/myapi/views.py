from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import filePostSerializer
from .models import file
from MyPersonalTrainer.settings import MEDIA_ROOT

import json
import os
import time
import subprocess
from natsort import natsorted

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class fileUploadApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = filePostSerializer

    def get(self, request):
        return Response("GET API")

    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        fs = FileSystemStorage()
        fs.save(file_uploaded.name, file_uploaded)
        content_type = file_uploaded.content_type
        fileName = file_uploaded.name
        filePath = MEDIA_ROOT+'/'+fileName
        file.objects.create(path=filePath)
        response = "POST API and you have uploaded a {} file".format(
            content_type)

        # Get All JsonFiles and sort them in a list
        JsonFiles_List = Existed_JsonFiles()

        # Check if there are Old JsonFiles and delete them
        if JsonFiles_List:
            for Jsonfile in JsonFiles_List:
                os.remove(Jsonfile)
            print("Old Jsonfiles deleted successfuly")
        else:
            print("there are no jsonfiles")

        # Calling Deep-Learning Model
        Calling_DL = subprocess.Popen(['python3', 'pose2.py', '-v', filePath])
        Calling_DL.wait()

        # Sorting the created JsonFiles from the Deep-Learning
        JsonFiles_List = Existed_JsonFiles()

        # Validate The Created JsonFiles
        if JsonFiles_List:
            valid_JsonFiles = []
            Invalid_JsonFiles = []
            for Jsonfile in JsonFiles_List:
                with open(Jsonfile) as f:
                    if ValidateJsonFile(f):
                        valid_JsonFiles.append(Jsonfile)
                    else:
                        Invalid_JsonFiles.append(Jsonfile)
            print("The Valid JsonFiles are:", valid_JsonFiles)
            print("The invalid JsonFiles are:", Invalid_JsonFiles)

        return Response(response)


def ValidateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as error:
        print(error)
        return False
    return True


def Existed_JsonFiles():
    path_to_json = '/home/awatef/MyPersonalTrainer'
    json_files = [pos_json for pos_json in os.listdir(
        path_to_json) if pos_json.endswith('.json')]
    Sorted_List = natsorted(json_files)
    return (Sorted_List)


'''
class Get_Path(APIView):
    permission_classes= ( AllowAny,)
    def get(self,request):
        #path=file.objects.get(id=2)
        path=file.objects.filter().order_by('-id')[0]
        FilePath=path.path
        return Response (FilePath)
'''
