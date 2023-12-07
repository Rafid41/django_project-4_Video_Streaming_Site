from django.contrib import admin
from App_Videos.models import Video_post, Category, Comment

# Register your models here.
admin.site.register(Video_post)
admin.site.register(Category)
admin.site.register(Comment)
