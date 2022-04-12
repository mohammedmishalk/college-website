from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('gallery/',views.gallery),
    path('about',views.about),
    path('messages',views.messages),
    path('administrative-staff',views.staff),
    path('management',views.management),
    path('facilitites',views.facilitites),
    path('contact',views.contact),
    path('instructions',views.instructions ),
    path('courses/<str:name>',views.courses),
    path('admission/',views.admission),
    path('admission/student-login',views.admUserLogin),
    path('admission/step/1',views.admUserData),
]
