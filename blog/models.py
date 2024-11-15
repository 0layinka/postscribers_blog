from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class postModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def comment_count(self):
        return self.comments.all().count()

    def comment(self):
        return self.comments.all()

    def __str__(self):
        return self.title
    

class comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(postModel, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=200)
    
    def __str__(self):
        return self.content
    
    