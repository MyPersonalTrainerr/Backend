from django.urls import path,include
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('signUpApi/',views.signUpApi.as_view(), name='signUpApi'),
    path('rest-auth/',include('rest_auth.urls')),
]