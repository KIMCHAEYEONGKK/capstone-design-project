from django.db import models
from django.conf import settings

class Service(models.Model):
    objects = None
    title = models.CharField(max_length=64, verbose_name="글 제목", blank=True)
    contents = models.TextField(verbose_name='글 내용', blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="등록시간")

    def __str__(self):
        return self.title


    class Meta:
        db_table = "UserService"
        verbose_name = "Service"