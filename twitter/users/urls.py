from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<username>/', views.useroverview, name='useroverview'),
    path('<username>/profileupdate/', views.profileupdate, name='profileupdate'),
]
