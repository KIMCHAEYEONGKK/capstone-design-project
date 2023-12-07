from django.db import models
from django.conf import settings

# from accounts.models import Account


# Create your models here.
class Food(models.Model):
    objects = None
    food_name = models.CharField(max_length=100, verbose_name="음식 이름")
    food_calorie = models.CharField(max_length=5, verbose_name="음식 칼로리")

    USERNAME_FIELD = "food_name"

    def __str__(self):
        return f"{self.id}  {self.food_name} ({self.food_calorie})kcal"

    class Meta:
        db_table = "UserFood"
        verbose_name = "food"


class Food_morning(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name="사용자",null=True)
    # m_name = models.ForeignKey('food.Food',on_delete=models.CASCADE,null=True,related_name="morning_name")
    # m_calorie = models.ForeignKey('food.Food',on_delete=models.CASCADE,null=True,related_name="morning_calorie")
    name = models.CharField(max_length=100, verbose_name="아침에 먹은 음식")
    calorie = models.CharField(max_length=5, verbose_name="아침에 먹은 칼로리")

    def __str__(self):
        return f"{self.id}  {self.name} ({self.calorie})kcal"

    class Meta:
        db_table = "Morning_Food"
        verbose_name = "morning_food"


class Food_lunch(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="사용자",null=True,on_delete=models.CASCADE,)
    # l_name = models.ForeignKey('food.Food', on_delete=models.CASCADE,null=True,related_name="lunch_name")
    # l_calorie = models.ForeignKey('food.Food', null=True,on_delete=models.CASCADE,related_name="lunch_calorie")
    name = models.CharField(max_length=100, verbose_name="점심에 먹은 음식")
    calorie = models.CharField(max_length=5, verbose_name="점심에 먹은 칼로리")


    def __str__(self):
        return f"{self.id}  {self.name} ({self.calorie})kcal"

    class Meta:
        db_table = "Lunch_Food"
        verbose_name = "lunch_food"



class Food_dinner(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="사용자",null=True,on_delete=models.CASCADE,)
    # d_name = models.ForeignKey('food.Food',max_length=100,null=True,on_delete=models.CASCADE,related_name="dinner_name")
    # d_calorie = models.ForeignKey('food.Food',max_length=5,null=True,on_delete=models.CASCADE,related_name="dinner_calorie")
    name = models.CharField(max_length=100, verbose_name="저녁에 먹은 음식")
    calorie = models.CharField(max_length=5, verbose_name = '저녁에 먹은 칼로리')


    def __str__(self):
        return f"{self.id}  {self.name} ({self.calorie})kcal"

    class Meta:
        db_table = "Dinner_Food"
        verbose_name = "dinner_food"


class Calorie(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  verbose_name="사용자",null=True,on_delete=models.CASCADE,)
    health_calorie = models.CharField(max_length=5, verbose_name="소비한 칼로리")
    # eat_cal_morning = models.CharField(max_length=5, verbose_name="아침에 섭취한 칼로리")
    # eat_cal_lunch = models.CharField(max_length=5, verbose_name="낮에 섭취한 칼로리")
    # eat_cal_dinner = models.CharField(max_length=5, verbose_name="저녁에 섭취한 칼로리")

    def __str__(self):
        return f"{self.user} ({self.health_calorie})kcal"

    class Meta:
        db_table = "UserCalorie"
        verbose_name = "calorie"

