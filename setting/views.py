import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Setting
from setting.forms import SettingForm
from django.core.exceptions import ObjectDoesNotExist
# from .models import Calendar
from django.contrib import messages


@login_required(login_url="accounts:login")
def inbody(request):
    if request.method == 'POST':
        form = SettingForm(request.POST)
        if form.is_valid():
            Set = Setting()
            Set.tall = form.cleaned_data['tall']
            Set.gender = form.cleaned_data['gender']
            Set.weight = form.cleaned_data['weight']  # form의 제목을 가져옴
            Set.fat = form.cleaned_data['fat']
            Set.muscle = form.cleaned_data['muscle']
            Set.target_weight = form.cleaned_data['target_weight']
            Set.datepicker1 = form.cleaned_data['datepicker1']
            Set.datepicker2 = form.cleaned_data['datepicker2']
            Set.user = request.user  # 현재 로그인한 사용자의 id
            Set.save()
            return redirect("setting:inbody_detail")  # 작성 후 글목록으로 이동

    else:
        form = SettingForm()
    return render(request, 'setting/inbody.html', {'form': form},)

# @login_required(login_url='accounts:login')
# def inbody(request):
#     if request.method =="POST":
#         Set = Setting()
#         Set.tall = request.POST["tall"]
#         Set.gender = request.POST['gender']
#         Set.weight = request.POST['weight']
#         Set.fat = request.POST['fat']
#         Set.muscle = request.POST['muscle']
#         Set.target_weight = request.POST['target_weight']
#         Set.datepicker1 = request.POST['datepicker1']
#         Set.datepicker2 = request.POST['datepicker2']
#         Set.user = request.user
#
#         return redirect('setting/inbody_detail/')
#     return render(request, 'setting/inbody.html')

@login_required(login_url="accounts:login")
def inbody_update(request,):
    sets = Setting.objects.get(user=request.user)
    if request.method == "POST":
        sets.tall = request.POST['tall']
        sets.gender = request.POST['gender']
        sets.fat = request.POST['fat']
        sets.weight = request.POST['weight']
        sets.now_weight = request.POST['now_weight']
        sets.muscle = request.POST['muscle']
        sets.target_weight = request.POST['target_weight']
        sets.datepicker1 = request.POST['datepicker1']
        sets.datepicker2 = request.POST['datepicker2']
        sets.user = request.user  # 현재 로그인한 사용자의 id

        sets.save()
        return redirect('/setting/inbody_detail/',)
    return render(request,'setting/inbody_update.html',{'sets':sets})

# @login_required(login_url="accounts:login")
# def inbody_detail(request):
#     sets =Setting.objects.get(user=request.user)
#     return render(request, 'setting/inbody_detail.html',{'sets':sets} )

@login_required(login_url="accounts:login")
def inbody_detail(request):
    try:
        sets = Setting.objects.get(user=request.user)
    except Setting.DoesNotExist:
        return redirect('setting:inbody')
    return render(request, 'setting/inbody_detail.html',{'sets':sets})


