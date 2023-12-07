from django.contrib import admin
from django.urls import path, include
from App_Videos import views

# display media/ image
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('videos/', include('App_Videos.urls')),
    path('', views.VideoList, name='video_lists'),
]

# media / image
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
