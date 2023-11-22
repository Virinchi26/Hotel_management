# from django.contrib import admin
from django.urls import path

from . import views

#mapping

urlpatterns = [
    path('', views.index, name='index'), #index page
    path('about', views.about, name='about'), #about page
    path('facilities', views.facilities, name='facilities'), #facilities page
    path('rooms', views.rooms, name='rooms'), #rooms page
    path('room_detail', views.room_detail, name='room_detail'), #room_detail page
    path('contactus', views.contactus, name='contactus'), #contactus page
    path('payment/', views.payment, name='payment'),
    # path('login_signup/', views.login_signup, name='login_signup'),
    # path('signup/', views.signup, name='signup'),
    path('register', views.register, name='register'), 
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout')


]
