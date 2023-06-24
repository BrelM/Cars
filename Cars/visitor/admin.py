from django.contrib import admin

from .models import *


class AnnoucementAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "price", "description", "model", "color", "image", "state", "builder", "car_type", "engine_type", "carburant", "power", "speed", "nb_horses")


admin.site.register(CarType)
admin.site.register(Builder)
admin.site.register(EngineType)
admin.site.register(Carburant)
admin.site.register(PowerType)
admin.site.register(SpeedType)
admin.site.register(Announcement, AnnoucementAdmin)
