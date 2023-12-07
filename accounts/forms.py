from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account


class SignupForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label="이름", required=True)
    age = forms.CharField(max_length=20, label="나이", required=True)
    # exercise = forms.ChoiceField(label="운동여부", widget=forms.Select(), choices=EXERCISE_CHOICES)
    # gender = forms.ChoiceField(label="성별", widget=forms.Select(), choices=GENDER_CHOICES)
    user_id = forms.CharField(max_length=20, label='아이디', required=True)
    password1 = forms.CharField(max_length=20, label='비밀번호', required=True)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="비밀번호 확인")
    phone = forms.CharField(max_length=11, label="번호")

    class Meta:
        model = Account
        fields = ("user_id", "name", "password1", "password2", "age",'phone')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '아이디을 입력해주세요.'},
        max_length=17,
        label='아이디'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '비밀번호를 입력해주세요.'},
        label='비밀번호'
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
                account= Account.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('username', '아이디가 존재하지 않습니다.')
                return

            from django.contrib.auth.hashers import check_password
            if not check_password(password, account.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
