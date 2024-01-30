from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm, LoginForm


# Create your views here.


# Home page
def index(request):
    return render(request, 'index.html')


# signup page
def user_signup(request):
    # if the request type is POST
    if request.method == 'POST':
        # create an object from the registration form with the request data
        form = UserCreationForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # saving the user in the database
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    # if the request type is GET
    else:
        # create an empty registration form object
        form = UserCreationForm()
    # rendering
    return render(request, 'signup.html', {'form': form})


# login page
def user_login(request):
    # if the request type is POST
    if request.method == 'POST':
        # create an object from the registration form with the request data
        form = LoginForm(request.POST)
        # saving the user in the database
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "!کاربری با این مشخصات یافت نشد")
                return redirect('login')
    # if the request type is GET
    else:
        # create an empty registration form object
        form = LoginForm()
    # rendering
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('home')

# TODO massage , clinic member views
