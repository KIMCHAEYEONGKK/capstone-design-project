from django.db import models
from django.conf import settings
# Create your models here.
class Exercise_cardio(models.Model):
    objects = None
    exercise_c_name = models.CharField(max_length=100, verbose_name="유산소 운동 이름")
    exercise_c_calorie = models.CharField(max_length=5, verbose_name="유산소 운동 칼로리")

    USERNAME_FIELD = "exercise_c_name"

    def __str__(self):
        return f"{self.id}  {self.exercise_c_name} ({self.exercise_c_calorie})kcal"

    class Meta:
        db_table = "UserExercise_cardio"
        verbose_name = "exercise_cardio"


class Exercise_upper(models.Model):
    objects = None
    exercise_u_name = models.CharField(max_length=100, verbose_name="상체 운동 이름")
    exercise_u_calorie = models.CharField(max_length=5, verbose_name="상체 운동 칼로리")

    USERNAME_FIELD = "exercise_u_name"

    def __str__(self):
        return f"{self.id}  {self.exercise_u_name} ({self.exercise_u_calorie})kcal"

    class Meta:
        db_table = "UserExercise_upper"
        verbose_name = "exercise_upper"


class Exercise_low(models.Model):
    objects = None
    exercise_l_name = models.CharField(max_length=100, verbose_name="하체 운동 이름")
    exercise_l_calorie = models.CharField(max_length=5, verbose_name="하체 운동 칼로리")

    USERNAME_FIELD = "exercise_l_name"

    def __str__(self):
        return f"{self.id}  {self.exercise_l_name} ({self.exercise_l_calorie})kcal"

    class Meta:
        db_table = "UserExercise_low"
        verbose_name = "exercise_low"

class Exercise_cardio_l(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="사용자", null=True)
    exercise_name = models.CharField(max_length=100, verbose_name="유산소 이름")
    exercise_calorie = models.CharField(max_length=5, verbose_name="유산소 칼로리")

    def __str__(self):
        return f"{self.id} {self.exercise_name} ({self.exercise_calorie})kcal"

    class Meta:
        db_table = "UserExerciseCardio_l"

class Exercise_upper_l(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="사용자", null=True)
    exercise_name = models.CharField(max_length=100, verbose_name="상체 이름")
    exercise_calorie = models.CharField(max_length=5, verbose_name="상체 칼로리")

    def __str__(self):
        return f"{self.id} {self.exercise_name} ({self.exercise_calorie})kcal"

    class Meta:
        db_table = "UserExerciseUpper_l"

class Exercise_low_l(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="사용자", null=True)
    exercise_name = models.CharField(max_length=100, verbose_name="하체 이름")
    exercise_calorie = models.CharField(max_length=5, verbose_name="하체 칼로리")

    def __str__(self):
        return f"{self.id} {self.exercise_name} ({self.exercise_calorie})kcal"

    class Meta:
        db_table = "UserExerciseLow_l"

# class Exercise_l(models.Model):
#     objects = None
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="사용자", null=True)
#     exercise_l_name = models.CharField(max_length=100, verbose_name="운동 이름")
#     exercise_l_calorie = models.CharField(max_length=5, verbose_name="운동 칼로리")
#
#     def __str__(self):
#         return f"{self.id}  {self.exercise_l_name} ({self.exercise_l_calorie})kcal"
#
#     class Meta:
#         db_table = "UserExercise_l"
#         verbose_name = "exercise_l"
