from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserChangeForm

class  createUser(UserCreationForm):
    password2 = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)  # Corrected capitalization
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={
            'username':"USERNAME",
            'first_name':'FirstName',
            'last_name':'LastName',
            'email':'Email'
        }

class Userinfo(UserChangeForm):
    password=None
    Model:User
    fields=['username','first_name','last_name','email']





