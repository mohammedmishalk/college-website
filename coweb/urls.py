
from django.contrib import admin
from django.urls import path,include
from api.urls import router
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/",include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
    path('manager/',include('sitemanager.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
