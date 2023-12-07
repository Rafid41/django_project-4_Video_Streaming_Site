from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category



# Create your models here.
class Video_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_videos')
    link=EmbedVideoField(blank=False)
    description = models.TextField(blank=True)
    title = models.CharField(max_length=264,  blank= False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # sort reverse of 'upload date'
        ordering = ('-upload_date',)





class Comment(models.Model):
    video = models.ForeignKey(Video_post, on_delete= models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_comment')
    comment=  models.TextField()
    comment_date= models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-comment_date',)  

    def __str__(self):
        return self.comment