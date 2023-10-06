# from django.contrib import admin
from django.urls import path

from . import views

#mapping

urlpatterns = [
    path('home', views.index, name='index'), #index page
    path('about', views.about, name='about'), #about page
    path('facilities', views.facilities, name='facilities'), #facilities page
    path('rooms', views.rooms, name='rooms'), #rooms page
    path('contactus', views.contactus, name='contactus'), #contactus page

]
