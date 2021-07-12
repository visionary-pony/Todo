from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .forms import TODOform
from .models import TODO
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOform()
        todos = TODO.objects.filter(user = user).order_by('status','priority').reverse()
        return render(request,'index.html', context = {'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html' ,{'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
        context = {
            "form" : form
        }
    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login')

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOform(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request , 'index.html' , context= {'form' : form})


def delete_todo(request,id):
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_status(request,id,status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

    