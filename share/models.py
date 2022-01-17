from django.db import models
from django.utils import timezone


#TODO:Djangoの中にあるユーザーモデルを使用して1対多のリレーションを組む
# https://noauto-nolife.com/post/django-foreignkey-user/
from django.contrib.auth.models import User

class Document(models.Model):

    dt = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    name = models.CharField(verbose_name="ファイル名", max_length=500)
    content   = models.FileField(verbose_name="ファイル", upload_to="share/document/content")
    mime = models.TextField(verbose_name="MIMEタイプ",null=True,blank=True)

    user = models.ForeignKey(User,verbose_name="投稿者",on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name
