from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('login',views.login_user,name='login'),
   path('regist',views.regist_user,name='regist'),
    path('logout',views.logout_user,name='logout')
   
]