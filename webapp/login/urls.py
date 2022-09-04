from cgitb import handler
from http import server
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
#handler404 = 'login.views.erorr_404'
#server500 = 'login.views.erorr_500'