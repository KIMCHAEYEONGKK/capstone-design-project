from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from setting.models import Setting
from food.models import Food
from exercise.models import Exercise_upper,Exercise_cardio,Exercise_low


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, name, user_id,age, phone,password=None):
        if not name:
            raise ValueError('must have user name')
        if not user_id:
            raise ValueError("must have userID.")
        user = self.model(
            name=name,
            user_id=user_id,
            age=age,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, age,name,user_id,phone, password):
        user = self.create_user(
            user_id=user_id,
            password=password,
            name=name,
            age=age,
            phone=phone,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Account(AbstractBaseUser):
    # user_setting = models.OneToOneField(Setting, on_delete=models.CASCADE,null=True)
    user_morning = models.ManyToManyField(Food ,related_name="morning_account" )
    user_lunch = models.ManyToManyField(Food, related_name="lunch_account")
    user_dinner = models.ManyToManyField(Food, related_name="dinner_account")
    user_exercise_c = models.ManyToManyField(Exercise_cardio, related_name="exercise_c_account")
    user_exercise_l = models.ManyToManyField(Exercise_low, related_name="exercise_l_account")
    user_exercise_u = models.ManyToManyField(Exercise_upper, related_name="exercise_u_account")
    id = None
    name = models.CharField(max_length=20, verbose_name='이름', default='')
    user_id = models.CharField(max_length=20, unique=True, default='', verbose_name="아이디")
    age = models.CharField(max_length=20, default='', verbose_name="나이")
    phone = models.CharField(max_length=11,default='', verbose_name="번호")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ['name','age','phone',]

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "UserAccounts"
        verbose_name = "accounts"

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

