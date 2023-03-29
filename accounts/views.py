from django.shortcuts import render, redirect
from . forms import AccountAuthenticationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from jobs.county import counties


def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
        else:
            print(form.errors)
            # return redirect('login_view')
    return render(request, 'accounts/register.html')


def technician_signup(request):
    context = {}
    context['counties'] = counties
    return render(request, 'accounts/TechSignUp.html', context)


def login_view(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                elif user.role == "technician":
                    return redirect('technician_dashboard')
                else:
                    return redirect('client_dashboard')
    return render(request, 'accounts/login.html')


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)

    return redirect('login_view')
