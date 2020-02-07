from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def useroverview(request, username):
    userprofile = get_object_or_404(CustomUser, username=username)
    tweets = userprofile.tweets.all()
    return render(request, 'useroverview.html', {'userprofile': userprofile, 'tweets': tweets})
