from . import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path("",views.home)
]

router = routers.DefaultRouter()
router.register('user',views.userViewsets,basename='user_api')
