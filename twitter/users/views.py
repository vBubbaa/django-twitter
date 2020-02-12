from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, Follow
from tweets.models import Tweet
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'home.html', {'tweets': tweets})

"""
- Custom signup view linking to the customuser creation form
- Tied to the AbstractUser class
"""
def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Get data from the form and authenticate, then login
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

"""
- Custom profile update view linking to the customuser change form
- Tied to the AbstractUser class
"""
@login_required
def profileupdate(request, username):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.cleaned_data.get('bio')
            form.save()
            # After we update the profile, redirect them to their overview page
            return redirect('useroverview', username=request.user.username)

    else:
        form = CustomUserChangeForm()
    return render(request, 'userupdate.html', {'form': form})

def useroverview(request, username):
    userprofile = get_object_or_404(CustomUser, username=username)
    tweets = userprofile.tweets.all()
    return render(request, 'useroverview.html', {'userprofile': userprofile, 'tweets': tweets})

"""

"""
@login_required
def follow(request):
    res = {}
    if request.method == 'GET':
        userid = request.GET['userid']
        following = get_object_or_404(CustomUser, pk=userid)
        follower = request.user

        # Check to see if the user already likes the tweet, if it does
        # then we delete the preexisting like
        if Follow.objects.filter(following=following, follower=follower).exists():
            Follow.objects.filter(following=following, follower=follower).delete()
            res['delete'] = True

        # If the like doesn't exist, then we create the like on the tweet
        else:
            Follow.objects.create(
                following=following,
                follower=follower
            )
            res['delete'] = False

        return JsonResponse(res, content_type='application/json')

    return render(request, 'newtweet.html')
