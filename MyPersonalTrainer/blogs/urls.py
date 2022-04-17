from django.urls import path

from blogs.views import (
    blogs_view,
    blog_detail_view
)


urlpatterns=[
    path('', blogs_view, name='blogs_view'),
    path('<slug:slug>/', blog_detail_view, name='blog_detail')
]