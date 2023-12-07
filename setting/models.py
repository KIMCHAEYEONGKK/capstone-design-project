from django.db import models
from django.conf import settings

GENDER_CHOICES = (
        ('MEN', '남자'),
        ('WOMEN', '여자')
    )
# Create your models here.
class Setting(models.Model):
    DoesNotExist = None
    objects = None
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name="사용자")
    weight = models.CharField(max_length=10, verbose_name="시작체중",)
    tall = models.CharField(max_length=3, verbose_name="키")
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,verbose_name="성별")
    now_weight = models.CharField(max_length=10, verbose_name="현재체중", null=True)
    fat = models.CharField(max_length=20, verbose_name="체지방량",)
    muscle = models.CharField(max_length=20, verbose_name="골격근량")
    target_weight = models.CharField(max_length=20, verbose_name="목표체중",)
    datepicker1 = models.CharField(max_length=10,verbose_name="시작날짜")
    datepicker2 = models.CharField(max_length=10,verbose_name="종료날짜")


    def __str__(self):
        return 'user={0}'.format(self.user)

    class Meta:
        db_table = "UserSetting"
        verbose_name = "setting"

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @classmethod
    def exists(cls):
        pass

# class Month(models.Model):
#     month = models.CharField(max_length=200, blank=True, null=True)
#
# class Day(models.Model):
#     day = models.CharField(max_length=200, blank=True, null=True)
