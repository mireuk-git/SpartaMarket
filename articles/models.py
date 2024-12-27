from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_DEFAULT,
        default="(알수없음)",
        related_name='my_articles', 
        blank=True
    )
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='liked_articles', 
        blank=True
    )