from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import FilePostSerializer
from .models import File
from MyPersonalTrainer.settings import MEDIA_ROOT
from MyPersonalTrainer.settings import AUTH_USER_MODEL as user
from NewUser.models import Account


import json
import os
import subprocess
from natsort import natsorted


class UploadVideo(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FilePostSerializer

    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        fs = FileSystemStorage()
        fs.save(file_uploaded.name, file_uploaded)
        content_type = file_uploaded.content_type
        fileName = file_uploaded.name
        filePath = MEDIA_ROOT+'/'+fileName
        File.objects.create(Path=filePath, UserProfile=request.user)
        response = "POST API and you have uploaded a {} file".format(
            content_type)

        # Get All JsonFiles and sort them in a list
        JsonFiles_List = ExistedJsonFiles()

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
        JsonFiles_List = ExistedJsonFiles()

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


def ExistedJsonFiles():
    path_to_json = '/home/awatef/MyPersonalTrainer'
    json_files = [pos_json for pos_json in os.listdir(
        path_to_json) if pos_json.endswith('.json')]
    Sorted_List = natsorted(json_files)
    return (Sorted_List)
