from django.urls import path,include
from . import views
#from rest_auth.urls
#from rest_auth.registration.urls'
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('signUpApi/',views.signUpApi.as_view(), name='signUpApi'),
    path('rest-auth/',include('rest_auth.urls')),
    path('registration/',include('rest_auth.registration.urls')),
    path('fileUploadApi/', views.fileUploadApi.as_view(), name='postFile'),
    
]
