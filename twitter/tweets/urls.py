from django.urls import path
from tweets import views

urlpatterns = [
    path('<username>/<int:tweet_id>', views.tweetoverview, name='tweet'),
    path('newtweet/', views.newtweet, name='newtweet'),
    path('newcomment/', views.newcomment, name='comment'),
    path('liketweet/', views.liketweet, name='liketweet'),
]
