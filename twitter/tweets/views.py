from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tweets.forms import TweetForm, CommentForm
from tweets.models import Tweet, Comment, Likes
from django.http import HttpResponse, JsonResponse
from django.contrib.humanize.templatetags.humanize import naturaltime
import json

"""
- View used by ajax to create a new Tweet object
- Ajax will send the data to this view and the view processes the information
  and creates the new object
"""
@login_required
def newtweet(request):
    res = {}
    if request.method =='POST':
        text = request.POST.get('text')
        user = request.user

        res['text'] = text
        res['username'] = user.username

        tweet = Tweet.objects.create(
            user = request.user,
            text = text,
        )

        # Pass the tweet that was just created for the prepend() method
        # that will update the page without refreshing with the new tweet
        res['tweetdate'] = naturaltime(tweet.created_date)
        res['tweetuser'] = tweet.user.username
        res['tweetpk'] = tweet.pk
        res['tweetlikecount'] = tweet.liked_tweet.count()

        # Send back the tweet and userurl for the success prepend() function
        # that will post the new tweet without refreshing
        res['tweeturl'] = tweet.get_absolute_url()
        res['userurl'] = user.get_absolute_url()

        return JsonResponse(res, content_type='application/json')

    return render(request, 'newtweet.html')

def tweetoverview(request, tweet_id, username):
    tweet = Tweet.objects.get(pk=tweet_id)
    # Sets the session tweetid to the clicked tweet
    request.session['tweetid'] = tweet.pk
    return render(request, 'tweetoverview.html', {'tweet': tweet})

# New comment endpoint hit when ajax sends a new comment POST
@login_required
def newcomment(request):
    res = {}
    if request.method =='POST':
        text = request.POST.get('text')
        user = request.user

        res['text'] = text
        res['username'] = user.username

        comment = Comment.objects.create(
            user = user,
            text = text,
            tweet = Tweet.objects.get(pk=request.POST.get('tweetid'))
        )

        res['createddate'] = naturaltime(comment.created_date)
        res['userurl'] = user.get_absolute_url()

        return JsonResponse(res, content_type='application/json')

    return render(request, 'newtweet.html')

"""
- the liketweet view is the endpoint we hit with ajax when a logged in user
  hits the like button (the heart <i>)
"""
@login_required
def liketweet(request):
    res = {}
    if request.method == 'GET':
        tweetid = request.GET['tweet_id']
        tweet = get_object_or_404(Tweet, pk = tweetid)
        user = request.user

        # Check to see if the user already likes the tweet, if it does
        # then we delete the preexisting like
        if Likes.objects.filter(tweet=tweet, user=user).exists():
            Likes.objects.filter(tweet=tweet, user=user).delete()
            res['delete'] = True

        # If the like doesn't exist, then we create the like on the tweet
        else:
            Likes.objects.create(
                user = user,
                tweet = tweet,
            )

        # Return the likecount so that we can update the likecount with the ajax response
        res['likecount'] = tweet.get_likes()

        return JsonResponse(res, content_type='application/json')

    return render(request, 'newtweet.html')
