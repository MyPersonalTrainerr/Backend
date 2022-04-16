from django.shortcuts import render


def blogs_view(request):
    return render(request, 'blogs/blogs.html')