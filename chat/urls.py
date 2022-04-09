from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),

    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('topics/', views.topicsPage, name="topics"),

    path('update-user/', views.updateUser, name="update-user"),
    path('activity/', views.activityPage, name="activity"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]
