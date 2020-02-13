from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<username>/', views.useroverview, name='useroverview'),
    path('<username>/userfollowers/', views.userfollowers, name='userfollowers'),
    path('<username>/userfollowing/', views.userfollowing, name='userfollowing'),
    path('<username>/profileupdate/', views.profileupdate, name='profileupdate'),
    path('follow/user', views.follow, name='follow'),
]
