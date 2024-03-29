from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    auther=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:50]
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

class Comment(models.Model):
    article=models.ForeignKey('article',on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    auther=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
    
