from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from setting.models import Setting

class SettingForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('MEN', '남자'),
        ('WOMEN', '여자')
    )

    tall = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="키")
    gender = forms.ChoiceField(label="성별", widget=forms.Select(), choices=GENDER_CHOICES)
    weight = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="시작체중")
    fat = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="체지방량")
    muscle = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="골격근량")
    target_weight = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="목표체중")
    datepicker1 = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
         max_length=10,label="시작날짜")
    datepicker2 = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=10, label="종료날짜")

    field_order = ["weight", "fat", "muscle", "target_weight",'tall','gender','exercise','datepicker1','datepicker2']

    class Meta:
        model = Setting
        fields = ["weight", "fat", "muscle", "target_weight",'tall','gender','datepicker1','datepicker2']
        exclude =['user', "now_weight"]