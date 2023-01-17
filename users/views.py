from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

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
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'User/signup.html', context = context)
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        context = {      
            'errors': form.errors,
            'form': UserCreationForm()          
        }
        
        return render(request, 'User/signup.html', context = context)
    
def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'User/profile.html', context = context)