from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'User/login.html', context = context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                context = {
                    'message': f'Welcome, {username}'
                }
                return render(request, 'index.html', context = context)
        form = AuthenticationForm()
        context = {
            'form': form,
            'errors': 'User or Password incorrect'
        }
        return render(request, 'User/login.html', context = context)

def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'User/signup.html', context = context)
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user  = form.save()
            Profile.objects.create(user = user, pfp = False)
            return redirect('login')
        
        context = {      
            'errors': form.errors,
            'form': RegisterForm()          
        }
        
        return render(request, 'User/signup.html', context = context)
    
@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'User/profile.html', context = context)

def pfp(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'pfp': user.profile.pfp
        })
        context ={
            'form': form
        }
        return render(request, 'User/edit.html', context = context)
    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.pfp = form.cleaned_data.get('pfp')
            user.profile.save()
            return redirect('profile')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'User/edit.html', context=context)