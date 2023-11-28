from django.contrib import admin

# Register your models here.

from . models import Event, Schedule, Partner, Award, Ticket


class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['event__eventName']


admin.site.register(Event)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Partner)
admin.site.register(Award)
admin.site.register(Ticket)