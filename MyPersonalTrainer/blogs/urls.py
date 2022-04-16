from django.urls import path

from blogs.views import blogs_view


urlpatterns=[
    path('', blogs_view, name='blogs_view')
]