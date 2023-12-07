from django.urls import path
from App_Videos import views

app_name = "App_Videos"

urlpatterns = [
    path("", views.VideoList, name="video_lists"),
    path('post_video/', views.CreateVideo.as_view(), name="post_video"),
    path('video_detail/<pk>/', views.video_detail, name="video_detail"),
    
]
