from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class createUser(UserCreationForm):
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': "USERNAME",
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'email': 'Email'
        }

class Userinfo(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'date_joined'
        ]

class AdminInfo(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'



    





