from django.db import models
from  django.contrib.auth.models import User
 
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    likes=models.ManyToManyField(User,related_name='liked_posts',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s Post"

 

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" Comment by {self.author.username}"