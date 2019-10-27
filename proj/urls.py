from django.contrib import admin
from django.urls import path, include
from mystorage import urls
from rest_framework import urls
from django.conf import settings #media file 위한 설정 1
from django.conf.urls.static import static #media file 위한 설정 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/',include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #media file