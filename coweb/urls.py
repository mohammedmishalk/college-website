
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('cowebui.urls')),
    path('admin/', admin.site.urls),
    path('manager/',include('sitemanager.urls')),
    path('user/',include('users.urls')),
    path('live-chat/',include('chat.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
