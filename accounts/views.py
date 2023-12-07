import random
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render
import datetime
import time
# Create your views here.
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, LoginForm
from django.db.models import Sum,Count
from django.contrib.auth import login as auth_login
import cv2
from exercise.models import Exercise_upper,Exercise_low,Exercise_cardio,Exercise_upper_l,Exercise_low_l,Exercise_cardio_l
from food.models import Food, Food_morning, Food_lunch, Food_dinner
from setting.models import Setting



# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            phone=form.cleaned_data.get('phone')
            user = authenticate(user_id=user_id, password=password, name=name,phone=phone,
                                age=age,)
            auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('accounts:login')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
                user_id = form.cleaned_data.get('user_id')
                password = form.cleaned_data.get('password')
                user = authenticate(user_id=user_id, password=password)
                auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')

                return redirect('setting:inbody')
    else:
        form=LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# def login(request):
#     if Setting.exists:
#         return redirect('setting:inbody_detail')
#     else:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user_id = form.cleaned_data.get('user_id')
#             password = form.cleaned_data.get('password')
#             user = authenticate(user_id=user_id, password=password)
#             auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#
#
#             return redirect('setting:inbody')
#
#     return render(request, 'accounts/login.html', {'form': form})


# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#
#         #     user_id = request.POST.get('user_id')
#         #     password = request.POST.get('password')
#         #     user = authenticate(request, user_id=user_id, password=password)
#         # if user is not None:
#         #     auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
#
#
#             return redirect('setting:inbody')
#     else:
#         form = LoginForm()
#
#
#     return render(request, 'accounts/login.html',{'form':form})



# def logout(request):
#     response = redirect('accounts:main')
#     response.delete_cookie('user_id')
#     response.delete_cookie('password')
#     logout(request)
#     return response

def logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url="accounts:login")
def home(request):
    try:
        sets = Setting.objects.get(user=request.user)
    except:
        return redirect('accounts:main')
    foods = Food.objects.all()
    M_Foods = Food_morning.objects.all()
    L_Foods = Food_lunch.objects.all()
    D_Foods = Food_dinner.objects.all()
    exercises_c = Exercise_cardio.objects.all()
    exercises_l = Exercise_low.objects.all()
    exercises_u = Exercise_upper.objects.all()
    exercises_c_l = Exercise_cardio_l.objects.all()
    exercises_u_l = Exercise_upper_l.objects.all()
    exercises_low_l = Exercise_low_l.objects.all()
    exercise_l_sum = Exercise_low_l.objects.aggregate(Sum('exercise_calorie'))
    exercise_c_sum = Exercise_cardio_l.objects.aggregate(Sum('exercise_calorie'))
    exercise_u_sum = Exercise_upper_l.objects.aggregate(Sum('exercise_calorie'))
    today = datetime.date.today()
    date1 = datetime.datetime.strptime(sets.datepicker1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(sets.datepicker2, '%Y-%m-%d').date()
    diff_date = date2 - today
    diff_date1 = date2 - date1
    exercise_l = exercise_l_sum.values()
    exercise_u = exercise_u_sum.values()
    exercise_c = exercise_c_sum.values()

    food_1 = random.choice(foods)
    food_2 = random.choice(foods)
    food_3 = random.choice(foods)
    food_4 = random.choice(foods)
    food_5 = random.choice(foods)
    food_6 = random.choice(foods)
    food_7 = random.choice(foods)
    food_8 = random.choice(foods)
    food_9 = random.choice(foods)

    e_1 = random.choice(exercises_c)
    e_2 = random.choice(exercises_c)
    e_3 = random.choice(exercises_c)
    e_4 = random.choice(exercises_u)
    e_5 = random.choice(exercises_u)
    e_6 = random.choice(exercises_u)
    e_7 = random.choice(exercises_l)
    e_8 = random.choice(exercises_l)
    e_9 = random.choice(exercises_l)

    a_tall = int(sets.tall) / 100
    a_weight = a_tall * a_tall

    bmi = int(sets.weight)/a_weight

    days=['월요일','회요일','수요일','목요일','금요일','토요일','일요일']
    a = datetime.datetime.today().weekday()
    b = days[a]
    # myList = [exercise_c_sum, exercise_l_sum, exercise_u_sum]
    #
    # arr = 0
    # for dic in myList:
    #     arr += dic['exercise_calorie__sum']
    #
    # print('arr = ', arr)

    return render(request,'accounts/home.html',context={'diff_date':diff_date,'diff_date1':diff_date1,'today':today,'b':b,'exercise_l_sum':exercise_l_sum,'exercise_c_sum':exercise_c_sum,
                'exercise_u_sum':exercise_u_sum,'date2':date2,'bmi':bmi,'a_tall':a_tall,'a_weight':a_weight,
                'exercise_l':exercise_l,'exercise_u':exercise_u,'exercise_c':exercise_c, 'sets':sets,'foods':foods,'M_Foods':M_Foods,'L_Foods':L_Foods,
                'D_Foods':D_Foods,'exercises_l':exercises_l,'exercises_c':exercises_c,'exercises_u':exercises_u,
                'exercises_c_l':exercises_c_l, 'exercises_u_l':exercises_u_l,'exercises_l_l':exercises_low_l,
                'food_1':food_1,'food_2':food_2,'food_3':food_3,'food_4':food_4,'food_5':food_5,'food_6':food_6,'food_7':food_7,
                'food_8':food_8,'food_9':food_9,'e_1':e_1,'e_2':e_2,'e_3':e_3,'e_4':e_4,'e_5':e_5,'e_6':e_6,'e_7':e_7,'e_8':e_8,'e_9':e_9})

def main(request):
    return render(request, 'accounts/main.html')

def main1(request):
    return render(request, 'accounts/main1.html')

def popup(request):
    sets = Setting.objects.get(user=request.user)
    a_tall = int(sets.tall) / 100
    a_weight = a_tall * a_tall

    bmi = int(sets.weight) / a_weight
    return render(request, 'accounts/popup.html',context={'sets':sets,'bmi':bmi})


BASE_URL = 'http://127.0.0.1.8000/api/v1/accounts/rest-auth/'
KAKAO_CALLBACK_URI = BASE_URL + 'kakao/callback/'
NAVER_CALLBACK_URI = BASE_URL + 'naver/callback/'
GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
