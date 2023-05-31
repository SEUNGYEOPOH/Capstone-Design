from django.contrib import admin
from django.urls import path
from tt import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dbdb_list/', views.dbdb, name='dbdb'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('time_feed/', views.time_feed, name='time_feed'),
    #path('tt/', views.tt, name='tt'),
]
