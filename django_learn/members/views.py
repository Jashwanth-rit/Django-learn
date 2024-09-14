
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
         messages.success(request,("there was an error in login, try again!"))
         return redirect('login')

    return render(request,'registration/login.html',{})

def regist_user(request):
    if request.method == "POST":
       form = RegisterUserForm(request.POST)
       if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          password  =  form.cleaned_data['password1']
          user = authenticate(username = username,password = password)
          login(request,user)
          return redirect('home')
    else:
       form  = RegisterUserForm()
    return render(request,'registration/register.html',{'form':form})


def logout_user(request):
    logout(request);
    

    return redirect('login')
