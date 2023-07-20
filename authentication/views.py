from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/')
        
    else:
        form = SignupForm()
    
    param = {
        'form': form,
    }
    
    return render(request, 'authentication/signup.html', param)


def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/')
        
    else:
        form = LoginForm()
    
    param = {
        'form': form,
        }

    return render(request, 'authentication/login.html', param)


class Logout(LogoutView):
    template_name = 'authentication/login.html'