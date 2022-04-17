from django.shortcuts import get_object_or_404, render

from blogs.models import Post


def blogs_view(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blogs/blogs.html', context={"posts": posts})

def blog_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogs/blog_detail.html', context={"post": post})