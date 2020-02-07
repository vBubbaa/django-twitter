from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tweets.forms import TweetForm
from tweets.models import Tweet

@login_required
def newtweet(request):
    if request.method =='POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet()
            tweet.user = request.user
            tweet.text = form.cleaned_data['text']
            tweet.save()
            return redirect('home')

    else:
        form = TweetForm()

    return render(request, 'newtweet.html', {'form': form})
