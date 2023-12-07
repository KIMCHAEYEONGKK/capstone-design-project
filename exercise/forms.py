from django import forms
from exercise.models import Exercise_upper,Exercise_cardio,Exercise_low,Exercise_upper_l,Exercise_low_l,Exercise_cardio_l

class Exercise_c_Form(forms.Form):
    c_exercise_calorie = forms.CharField(max_length=5, label="유산소 운동 칼로리", required=True)
    c_exercise_name = forms.CharField(max_length=20, label="유산소 운동 이름", required=True)

    class Meta:
        model = Exercise_cardio
        fields = ['c_exercise_calorie','c_exercise_name']

class Exercise_u_Form(forms.Form):
    u_exercise_calorie = forms.CharField(max_length=5, label="상체 운동 칼로리", required=True)
    u_exercise_name = forms.CharField(max_length=20, label="상체 운동 이름", required=True)

    class Meta:
        model = Exercise_upper
        fields = ['c_exercise_calorie','c_exercise_name']

class Exercise_L_Form(forms.Form):
    l_exercise_calorie = forms.CharField(max_length=5, label="하체 운동 칼로리", required=True)
    l_exercise_name = forms.CharField(max_length=20, label="하체 운동 이름", required=True)

    class Meta:
        model = Exercise_low
        fields = ['l_exercise_calorie','l_exercise_name']


class Exercises_c_Form(forms.Form):
    exercises_c_calorie = forms.CharField(max_length=5, label="운동 칼로리", required=True)
    exercises_c_name = forms.CharField(max_length=20, label="운동 이름", required=True)

    class Meta:
        model = Exercise_cardio_l
        fields = ['exercises_c_calorie','exercises_c_name']


class Exercises_l_Form(forms.Form):
    exercises_l_calorie = forms.CharField(max_length=5, label="운동 칼로리", required=True)
    exercises_l_name = forms.CharField(max_length=20, label="운동 이름", required=True)

    class Meta:
        model = Exercise_low_l
        fields = ['exercises_l_calorie','exercises_l_name']

class Exercises_u_Form(forms.Form):
    exercises_u_calorie = forms.CharField(max_length=5, label="운동 칼로리", required=True)
    exercises_u_name = forms.CharField(max_length=20, label="운동 이름", required=True)

    class Meta:
        model = Exercise_upper_l
        fields = ['exercises_u_calorie','exercises_u_name']
