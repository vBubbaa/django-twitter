from django.contrib import admin
from django.urls import path, include
from tweets import views as tweetviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweets.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('signup/', tweetviews.signup, name='signup')
]
