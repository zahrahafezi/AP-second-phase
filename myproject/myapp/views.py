from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm, LoginForm, SignupForm


# Create your views here.


# Home page
def index(request):
    return render(request, 'index.html')


# signup page
def user_signup(request):
    # if the request type is POST
    if request.method == 'POST':
        # create an object from the registration form with the request data
        # !!!!!!!!!
        form = SignupForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # اگر کاربر بیمار باشد
            if form.cleaned_data['role'] == 'patient':
                # انجام اقدامات مربوط به کاربر بیمار
                pass
            # اگر کاربر منشی باشد
            elif form.cleaned_data['role'] == 'secretary':
                # انجام اقدامات مربوط به کاربر منشی
                pass
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
        form = SignupForm()
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
            user_type = form.cleaned_data['user_type']

            user = authenticate(request, username=username, password=password)

            if user:
                if user.userrole.role == user_type:
                    # login the user
                    login(request, user)
                    # redirect the user to the appropriate page based on the user type
                    if user_type == 'patient':
                        return redirect('patient')
                    elif user_type == 'secretary':
                        return redirect('secretary')
                else:
                    # show an error message that the user type is incorrect
                    messages.error(request, "!نوع کاربری وارد شده صحیح نیست")
                    return redirect('login')
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


# new
def patient(request):
    # check if the user is logged in and is a patient
    if request.user.is_authenticated and request.user.userrole.role == 'patient':
        # render the patient page
        return render(request, 'patient.html')
    else:
        # redirect to the login page
        return redirect('login')


# new
def secretary(request):
    # check if the user is logged in and is a secretary
    if request.user.is_authenticated and request.user.userrole.role == 'secretary':
        # render the secretary page
        return render(request, 'secretary.html')
    else:
        # redirect to the login page
        return redirect('login')
