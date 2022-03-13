from django.urls import path, include
from . import views


urlpatterns = [
    path('UploadVideo/', views.UploadVideo.as_view(), name='UploadVideo'),
]
