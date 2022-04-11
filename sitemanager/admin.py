from django.contrib import admin

from sitemanager.models import Staf, Students, Teachers, TimeTable

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Staf)
admin.site.register(TimeTable)

