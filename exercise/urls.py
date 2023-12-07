from django.urls import path
from .import views

app_name = 'exercise'

urlpatterns =[
    path('exercise_cardio/',views.exercise_cardio, name="exercise_cardio"),
    path('exercise_list/',views.exercise_list, name="exercise_list"),
    path('exercise_low/',views.exercise_low, name="exercise_low"),
    path('exercise_upper/', views.exercise_upper, name="exercise_upper"),
    path('exercise/', views.exercise, name='exercise')
]