from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE) #모델지우면 그 모델과 관련한 모든 것 지움
    title = models.CharField(max_length = 30)
    body = models.TextField()

class Album(models.Model): #image파일을 효율적으로 관리하기 위해 pip install Pillow 하기
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE) #모델지우면 그 모델과 관련한 모든 것 지움
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length = 100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE) #모델지우면 그 모델과 관련한 모든 것 지움
    myfile = models.FileField(blank = False, null = False, upload_to="files")
    desc = models.CharField(max_length = 100)