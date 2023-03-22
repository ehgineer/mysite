from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # 비밀번호가 맞지 않습니다
    error_messages = {
        'password_mismatch': "The two password fields didn't match."
    }
    # 회원가입시 입력 사항
    # 나이, 지역은 입력, #성별 선택
    age = forms.CharField(label="나이")
    
    region = forms.CharField(label="지역")

    gender = forms.ChoiceField(required=True, label= '성별', choices = (
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
    ))
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "age", "region", "gender")