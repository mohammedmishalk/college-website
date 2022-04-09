from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard),
    path('login/',views.userLogin),
    path('logout/',views.userLogout),
    path('send-notification/',views.sendNotification)
]
