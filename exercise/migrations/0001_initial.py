# Generated by Django 4.2.5 on 2023-11-30 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise_cardio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_c_name",
                    models.CharField(max_length=100, verbose_name="유산소 운동 이름"),
                ),
                (
                    "exercise_c_calorie",
                    models.CharField(max_length=5, verbose_name="유산소 운동 칼로리"),
                ),
            ],
            options={
                "verbose_name": "exercise_cardio",
                "db_table": "UserExercise_cardio",
            },
        ),
        migrations.CreateModel(
            name="Exercise_low",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_l_name",
                    models.CharField(max_length=100, verbose_name="하체 운동 이름"),
                ),
                (
                    "exercise_l_calorie",
                    models.CharField(max_length=5, verbose_name="하체 운동 칼로리"),
                ),
            ],
            options={
                "verbose_name": "exercise_low",
                "db_table": "UserExercise_low",
            },
        ),
        migrations.CreateModel(
            name="Exercise_upper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_u_name",
                    models.CharField(max_length=100, verbose_name="상체 운동 이름"),
                ),
                (
                    "exercise_u_calorie",
                    models.CharField(max_length=5, verbose_name="상체 운동 칼로리"),
                ),
            ],
            options={
                "verbose_name": "exercise_upper",
                "db_table": "UserExercise_upper",
            },
        ),
        migrations.CreateModel(
            name="Exercise_upper_l",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_name",
                    models.CharField(max_length=100, verbose_name="상체 이름"),
                ),
                (
                    "exercise_calorie",
                    models.CharField(max_length=5, verbose_name="상체 칼로리"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사용자",
                    ),
                ),
            ],
            options={
                "db_table": "UserExerciseUpper_l",
            },
        ),
        migrations.CreateModel(
            name="Exercise_low_l",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_name",
                    models.CharField(max_length=100, verbose_name="하체 이름"),
                ),
                (
                    "exercise_calorie",
                    models.CharField(max_length=5, verbose_name="하체 칼로리"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사용자",
                    ),
                ),
            ],
            options={
                "db_table": "UserExerciseLow_l",
            },
        ),
        migrations.CreateModel(
            name="Exercise_cardio_l",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise_name",
                    models.CharField(max_length=100, verbose_name="유산소 이름"),
                ),
                (
                    "exercise_calorie",
                    models.CharField(max_length=5, verbose_name="유산소 칼로리"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사용자",
                    ),
                ),
            ],
            options={
                "db_table": "UserExerciseCardio_l",
            },
        ),
    ]
