from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE) #모델지우면 그 모델과 관련한 모든 것 지움
    title = models.CharField(max_length = 30)
    body = models.TextField()