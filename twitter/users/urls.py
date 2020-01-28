from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup')
]
