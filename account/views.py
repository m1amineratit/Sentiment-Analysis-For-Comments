from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    # redirect authenticated users
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # support next param
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'auth/register.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('login')