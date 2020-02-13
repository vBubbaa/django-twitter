from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('tweet/', include('tweets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
