import datetime
import time
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from exercise.forms import Exercises_l_Form,Exercises_c_Form,Exercises_u_Form
from exercise.models import Exercise_cardio_l,Exercise_upper_l,Exercise_low_l,Exercise_cardio,Exercise_low,Exercise_upper
from django.db.models import Sum,Count
from setting.models import Setting

@login_required(login_url="accounts:login")
def exercise(request):
    # setting = Setting.objects.get(user=request.user)
    return render(request, 'exercise/exercise.html',)

@login_required(login_url="accounts:login")
def exercise_cardio(request):
    exercises_c = Exercise_cardio.objects.all()
    # setting = Setting.objects.get(user=request.user)
    if request.method == "POST":
            Exercises_c = Exercise_cardio_l()
            Exercises_c.exercise_name = request.POST['exercise_name']
            Exercises_c.exercise_calorie = request.POST['exercise_calorie']
            Exercises_c.user = request.user
            Exercises_c.save()
            return redirect('exercise:exercise_list')
    return render(request, 'exercise/exercise_cardio.html', context={'exercises_c':exercises_c,})

@login_required(login_url="accounts:login")
def exercise_upper(request):
    exercises_u = Exercise_upper.objects.all()

    if request.method == "POST":
            Exercises_u = Exercise_upper_l()
            Exercises_u.exercise_name = request.POST['exercise_name']
            Exercises_u.exercise_calorie = request.POST['exercise_calorie']
            Exercises_u.user = request.user
            Exercises_u.save()
            return redirect('exercise:exercise_list')
    return render(request, 'exercise/exercise_upper.html', context={'exercises_u':exercises_u,})

@login_required(login_url="accounts:login")
def exercise_low(request):
    exercises_low = Exercise_low.objects.all()

    if request.method =="POST":
            Exercises_l = Exercise_low_l()
            Exercises_l.exercise_name = request.POST['exercise_name']
            Exercises_l.exercise_calorie = request.POST['exercise_calorie']
            Exercises_l.user = request.user
            Exercises_l.save()
            return redirect('exercise:exercise_list')
    return render(request, 'exercise/exercise_low.html', context={'form':Exercises_l_Form, 'exercises_low':exercises_low,})

@login_required(login_url="accounts:login")
def exercise_list(request):
    exercises_c_l = Exercise_cardio_l.objects.all()
    exercises_low_l = Exercise_low_l.objects.all()
    exercises_u_l = Exercise_upper_l.objects.all()
    sets = Setting.objects.get(user=request.user)
    exercise_l_sum = Exercise_low_l.objects.aggregate(Sum('exercise_calorie'))['exercise_calorie__sum']
    exercise_c_sum = Exercise_cardio_l.objects.aggregate(Sum('exercise_calorie'))['exercise_calorie__sum']
    exercise_u_sum = Exercise_upper_l.objects.aggregate(Sum('exercise_calorie'))['exercise_calorie__sum']
    today = datetime.today()
    date1 = datetime.strptime(sets.datepicker1, '%Y-%m-%d')
    date2 = datetime.strptime(sets.datepicker2, '%Y-%m-%d')
    diff_date = date2 - today
    # exercise_l = exercise_l_sum.values()
    # exercise_u = exercise_u_sum.values()
    # exercise_c = exercise_c_sum.values()

    if exercise_u_sum  == None:
        exercise_u_sum =0
    if exercise_c_sum == None:
        exercise_c_sum = 0
    if exercise_l_sum == None:
        exercise_l_sum = 0

    arr=sum([exercise_l_sum,exercise_c_sum,exercise_u_sum])
    # for dic in myList:
    #     arr += dic




    # for exercise_c_calorie_l in exercises_c_l:
    #     dict_list[exercise_c_calorie_l] += exercise_c_calorie_l
    # for exercise_u_calorie_l in exercises_u_l:
    #     dict_list[exercise_u_calorie_l] += exercise_u_calorie_l
    # for exercise_l_calorie_l in exercises_low_l:
    #     dict_list[exercise_l_calorie_l] += exercise_l_calorie_l
    #


    return render(request, 'exercise/exercise_list.html',
                  context={'diff_date':diff_date,'today':today,'arr':arr,"exercises_c_l":exercises_c_l, "exercises_low_l":exercises_low_l, "exercises_u_l":exercises_u_l,
                          "exercise_l_sum":exercise_l_sum, 'exercise_u_sum':exercise_u_sum, 'exercise_c_sum':exercise_c_sum,
                           'sets':sets,
                           })
