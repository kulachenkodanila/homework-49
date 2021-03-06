from django.contrib import admin

from webapp.models import Work, Type, Status


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['description', 'status', 'type']
    fields = ['summary', 'description', 'status', 'type', 'created_at']
    readonly_fields = ['updated_at', 'created_at']


admin.site.register(Work, WorkAdmin),
admin.site.register(Type)
admin.site.register(Status)

# Register your models here.
