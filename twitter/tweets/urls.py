from django.urls import path
from tweets import views

urlpatterns = [
    path('newtweet/', views.newtweet, name='newtweet')
]
