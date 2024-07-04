from django.shortcuts import render
from .forms import createUser,Userinfo
from django.contrib.auth import login,logout,update_session_auth_hash
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
        form=createUser(request.POST)
        if form.is_valid():           
            user=form.save()
            messages.success(request,"FORMS SAVED SUCCESSFULLY")
            login(request,user)    
  
    else:
        form=createUser()
    
    return render(request,'user.html',{'form':form})


def LOGIN(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')   
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request, "Invalid username or password")
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'fm': fm})


def profile(request):
    if request.user.is_authenticated:
       return render(request,'profile.html',{'name':request.user})   
    else:
        return HttpResponseRedirect('/login/')
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def changePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                user = fm.save()
                update_session_auth_hash(request, user)  # Update session auth hash with the updated user object
                messages.success(request, "Password changed successfully")
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request, "Please correct the errors below.")
                return render(request, 'passwold.html', {'fm': fm})
        else:
            fm = SetPasswordForm(user=request.user)
        
        return render(request, 'passwold.html', {'fm': fm})
    
    else:
        return HttpResponseRedirect('/login/')

def changeWO(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                user = fm.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed successfully")
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request, "Please correct the errors below.")
                return render(request, 'changepass.html', {'fm': fm})
        else:
            fm = PasswordChangeForm(user=request.user)
        
        return render(request, 'changepass.html', {'fm': fm})
    
    else:
        return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.is_authenticated:
       return render(request,'profile.html',{'name':request.user})   
    else:
        return HttpResponseRedirect('/login/')
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')



def test(request):
  pass
def userInfo(request):
    pass



