from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
 

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return render(request, 'home.html')

@login_required
def loginHome(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print("Successful")
                return redirect('/home/')
            else:
                print('User not found')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'Registry/login.html', {"form": form})

'''
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register/app')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'Registry/signup.html', args)
'''