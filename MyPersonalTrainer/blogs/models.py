from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    slug       = models.SlugField(max_length=128, unique=True)
    title      = models.CharField(max_length=128, unique=True)
    content    = models.TextField()
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status     = models.IntegerField(choices=STATUS, default=0)
    # tags

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title