from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tweets.forms import TweetForm, CommentForm
from tweets.models import Tweet, Comment
from django.http import HttpResponse
import json

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

def tweetoverview(request, tweet_id, username):
    tweet = Tweet.objects.get(pk=tweet_id)
    request.session['tweetid'] = tweet.pk
    return render(request, 'tweetoverview.html', {'tweet': tweet})

@login_required
def newcomment(request):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.user = request.user
            comment.tweet = Tweet.objects.get(pk=request.session.get('tweetid'))
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect(comment.tweet.get_absolute_url())

    else:
        form = CommentForm()

    return render(request, 'newcomment.html', {'form': form})
