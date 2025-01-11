from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('base:index')
            else:
                messages.error(request, 'Daxil edilmiş məlumatlar yanlışdır.')
        else:
            messages.error(request, 'Formada səhv var.')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            
            user.phone_number = phone_number
            user.save()

            messages.success(request, 'Qeydiyyat uğurla tamamlandı!')
            return redirect('user:login')
    else:
        form = RegisterForm()
    
    return render(request, 'user/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')


def account(request):
    return render(request, 'user/account.html')


def change_password(request):
    return render(request, 'user/changePassword.html')


def payment(request):
    return render(request, 'payment.html')


def send_email_code(request):
    return render(request, 'user/sendEmailCode.html')


def six_digit_password(request):
    return render(request, 'user/sixdigitsPassword.html')