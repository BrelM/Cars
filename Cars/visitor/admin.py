from django.contrib import admin

from .models import *


class AnnoucementAdmin(admin.ModelAdmin):
    list_display = ("car", "price", "description")


admin.site.register(CarType)
admin.site.register(Builder)
admin.site.register(EngineType)
admin.site.register(Carburant)
admin.site.register(PowerType)
admin.site.register(SpeedType)
admin.site.register(Engine)
admin.site.register(Car)
admin.site.register(Announcement, AnnoucementAdmin)
