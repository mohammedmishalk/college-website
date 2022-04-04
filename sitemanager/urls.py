from . import views
from django.urls import path

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("admin_login/",views.admin_login),
    path('add/student',views.add_student),
    path('add/teacher',views.add_teacher),
    path('add/staf',views.add_staf),
    path('edit/teacher/<int:u_id>',views.edit_teacher),
    path('edit/student/<int:u_id>',views.edit_student),
    path('edit/staf/<int:u_id>',views.edit_staf),

]
