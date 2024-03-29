from . import views
from users.views import gallery, userLogout
from django.urls import path

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("admin_login/",views.admin_login),
    path("logout/",userLogout),
    path('dept',views.dept),
    path('dept/<int:pk>',views.dept_edit),
    path('add/student',views.add_student),
    path('add/teacher',views.add_teacher),
    path('add/staf',views.add_staf),
    path('sylabus',views.sylabus),
    path('time-table',views.timeTable),
    path('time-table/fech',views.fech_time_table),
    path('notification',views.sendNotification),
    path('in-box',views.leaveRequestView),
    path('in-box/<int:pk>/<int:option>',views.leaveRequestcontrol),
    path('gallery',views.gallery),
    path('gallery/<int:pk>/<int:option>',views.gallery_action),
    path('delete/user/<int:u_id>',views.remove_user),
    path('edit/teacher/<int:u_id>',views.edit_teacher),
    path('edit/student/<int:u_id>',views.edit_student),
    path('edit/staf/<int:u_id>',views.edit_staf),

]
