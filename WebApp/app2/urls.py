from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup')
]
