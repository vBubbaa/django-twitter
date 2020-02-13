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
        form = CustomUserCreationForm(request.POST, request.FILES)
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
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.cleaned_data.get('bio')
            form.cleaned_data.get('location')
            form.cleaned_data.get('website')
            form.cleaned_data.get('profilepicture')
            form.save()
            # After we update the profile, redirect them to their overview page
            return redirect('useroverview', username=request.user.username)

    else:
        form = CustomUserChangeForm()
    return render(request, 'userupdate.html', {'form': form})

def useroverview(request, username):
    # The profile of the user for the overview page
    userprofile = get_object_or_404(CustomUser, username=username)

    # Grabs the number of followers the user has
    followers = Follow.objects.filter(following=userprofile).count()

    # Grabs the people the user follows
    following = Follow.objects.filter(follower=userprofile).count()

    tweets = userprofile.tweets.all()
    return render(
        request,
        'useroverview.html',
        {
            'userprofile': userprofile,
            'tweets': tweets,
            'followers': followers,
            'following': following
        }
    )

# Returns the number of followers the user has queried by a username
def userfollowers(request, username):
    user = get_object_or_404(CustomUser, username=username)
    followers = Follow.objects.filter(following=user).all()

    return render(request, 'userfollowers.html', {'followers': followers, 'user': user})

# Returns the number people a user are following
def userfollowing(request, username):
    user = get_object_or_404(CustomUser, username=username)
    following = Follow.objects.filter(follower = user).all()

    return render(request, 'userfollowing.html', {'following': following, 'user': user})


"""
- Endpoint hit via ajax when a user clicks the follow button
- Checks if the user is already following, if they are not it makes a follow object
- Else it deletes the follow object (unfollows)
"""
@login_required
def follow(request):
    res = {}
    if request.method == 'GET':
        userid = request.GET['userid']
        following = get_object_or_404(CustomUser, pk=userid)
        follower = request.user

        # Check to see if the user already follows, if they do, remove the follow object
        if Follow.objects.filter(following=following, follower=follower).exists():
            Follow.objects.filter(following=following, follower=follower).delete()
            # set the delete action to true so we can render that in the frontend
            res['delete'] = True

        # If the user isnt following them already, create the follow object
        # and set the delete action to false so we can render that in the frontend
        else:
            Follow.objects.create(
                following=following,
                follower=follower
            )
            res['delete'] = False

        # Return the count of followers after action happened to update frontend
        res['newFollowerCount'] = Follow.objects.filter(following=following).count()

        return JsonResponse(res, content_type='application/json')
