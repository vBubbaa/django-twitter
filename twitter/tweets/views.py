from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tweets.forms import TweetForm, CommentForm
from tweets.models import Tweet, Comment
from django.http import HttpResponse, JsonResponse
import json

@login_required
def newtweet(request):
    res = {}
    if request.method =='POST':
        text = request.POST.get('text')
        print('text@@@@@@@@@@@@@' + str(text))
        user = request.user

        res['text'] = text
        res['username'] = user.username

        tweet = Tweet.objects.create(
            user = request.user,
            text = text,
        )

        res['tweetdate'] = tweet.created_date
        res['tweetuser'] = tweet.user.username
        res['tweetpk'] = tweet.pk

        res['tweeturl'] = tweet.get_absolute_url()
        res['userurl'] = user.get_absolute_url()

        return JsonResponse(res, content_type='application/json')

    return render(request, 'newtweet.html')

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
