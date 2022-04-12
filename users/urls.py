from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard),
    path('gallery/',views.gallery),
    path('leave-request',views.leaveRequest),
    path('time-table',views.timeTable),
    path('sylabus',views.sylabus),
    path('in-box',views.inBox),
    path('login/',views.userLogin),
    path('logout/',views.userLogout),
    path('notification',views.sendNotification)
]
