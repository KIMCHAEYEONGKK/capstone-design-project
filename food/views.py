from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CalorieForm,FoodForm,MorningForm,LunchForm,DinnerForm
from .models import Food,Calorie,Food_morning,Food_lunch,Food_dinner
from exercise.models import Exercise_upper,Exercise_upper_l,Exercise_low_l,Exercise_cardio_l

from django.db.models import Sum
from setting.models import Setting

@login_required(login_url="accounts:login")
def calorie(request):
    return render(request, 'food/food.html',)

@login_required(login_url="accounts:login")
def food_list(request):
    food_morning = Food_morning.objects.all()
    food_lunch = Food_lunch.objects.all()
    food_dinner = Food_dinner.objects.all()
    morning = Food_morning.objects.aggregate(Sum('calorie'))['calorie__sum']
    lunch = Food_lunch.objects.aggregate(Sum('calorie'))['calorie__sum']
    dinner = Food_dinner.objects.aggregate(Sum('calorie'))['calorie__sum']
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


    if morning == None:
        morning = 0
    if lunch == None:
        lunch = 0
    if dinner == None:
        dinner =0



    arr1 = sum([exercise_l_sum, exercise_c_sum, exercise_u_sum])
    arr2 = sum([morning, lunch, dinner])

    # arr1 = exercise_l_sum + exercise_u_sum + exercise_c_sum

    # myList = [exercise_c_sum, exercise_l_sum, exercise_u_sum]
    # arr1 = 0
    # for dic in myList:
    #     arr1 += dic['exercise_calorie__sum']
    # myList = [exercise_c_sum,exercise_u_sum,exercise_l_sum]
    # arr1 = 0
    # for dic in myList:
    #     arr1 += dic['exercise_calorie__sum']
    #
    #
    # myList1 = [morning, lunch, dinner]
    # arr2 = 0
    # for dic in myList1:
    #     arr2 += dic['calorie__sum']


    return render(request, 'food/food_list.html',
                  context={'exercises_low_l':exercises_low_l,'exercise_c_sum':exercise_c_sum,'exercise_l_sum':exercise_l_sum,'exercise_u_sum':exercise_u_sum,'exercises_u_l':exercises_u_l,'diff_date':diff_date,
                           'arr1':arr1,'arr2':arr2,
                           'exercises_c_l':exercises_c_l,"morning":morning,
                           "lunch":lunch, "dinner":dinner, "food_morning":food_morning,"food_lunch":food_lunch,
                           "food_dinner":food_dinner,})

@login_required(login_url="accounts:login")
def food_morning(request):
    Foods = Food.objects.all()
    if request.method == "POST":
        form = MorningForm(request.POST)
        if form.is_valid():
            foods = Food_morning()
            foods.name = form.cleaned_data['name']
            foods.calorie = form.cleaned_data['calorie']
            foods.user = request.user
            foods.save()
            return redirect('food:food_list')

    return render(request, 'food/food_morning.html', context={'form':MorningForm, 'Foods':Foods})


@login_required(login_url="accounts:login")
def food_lunch(request):
    Foods = Food.objects.all()
    if request.method == "POST":
        form = LunchForm(request.POST)
        if form.is_valid():
            FOOD = Food_lunch()
            FOOD.name = form.cleaned_data['name']
            FOOD.calorie = form.cleaned_data['calorie']
            FOOD.user = request.user
            FOOD.save()
            return redirect('food:food_list')

    return render(request, 'food/food_lunch.html',context={'form':LunchForm, 'Foods':Foods})

@login_required(login_url="accounts:login")
def food_dinner(request):
    Foods = Food.objects.all()
    if request.method == "POST":
        form = DinnerForm(request.POST)
        if form.is_valid():
            FOOD = Food_dinner()
            FOOD.name = form.cleaned_data['name']
            FOOD.calorie = form.cleaned_data['calorie']
            FOOD.user = request.user
            FOOD.save()
            return redirect('food:food_list')

    return render(request, 'food/food_dinner.html', context={'form':DinnerForm, 'Foods':Foods})

# def search_food(request):
#     qs = Food.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(name_icontains=q)
#     return render(request, 'food/food.morning.html',{'Foods':qs, 'q':q,})
#
# def search_food(request):
#     Foods = Food.objects.all()
#     return render(request, 'food/food_morning.html',{'Foods':Foods})


# def search_lunch(request):
#     Foods = Food.objects.all()
#     return render(request, 'food/food_lunch.html', {'Foods':Foods})
#
# def search_dinner(request):
#     Foods = Food.objects.all()
#     return render(request, 'food/food_lunch.html',{'Foods':Foods})