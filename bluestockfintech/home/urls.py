from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.adminlogin, name='login'),
    path('signup/', views.adminsignup, name='signup'),
    path('forgetpass/', views.adminforgetpass, name='forgetpass'),
    path('upcomingipo/', views.upcomingIPO, name='upcomingipo'),
    path('registeripo/', views.registerIPO, name='registeripo'),    
]