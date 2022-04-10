from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('gallery',views.gallery),
    path('admission/',views.admission),
    path('admission/student-login',views.admUserLogin),
    path('admission/step/1',views.admUserData),
    path('user/',views.dashboard),
    path('user/gallery/',views.gallery),
    path('user/leave-request',views.leaveRequest),
    path('user/in-box',views.inBox),
    path('user/login/',views.userLogin),
    path('user/logout/',views.userLogout),
    path('user/notification',views.sendNotification)
]
