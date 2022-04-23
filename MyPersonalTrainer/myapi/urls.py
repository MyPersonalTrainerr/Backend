from django.urls import path,include
from . import views
#from rest_auth.urls
#from rest_auth.registration.urls'
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('fileUploadApi/', views.fileUploadApi.as_view(), name='postFile'),
    path('getStatus/',views.Get_Status.as_view(),name='GetStatus'),
]
