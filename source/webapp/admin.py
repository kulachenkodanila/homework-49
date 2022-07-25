from django.contrib import admin

from webapp.models import Work, Type, Status, Project


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'created_at', 'updated_at', 'projects']
    list_filter = ['status', 'created_at']
    list_display_links = ['summary']
    search_fields = ['description', 'status', 'types']
    fields = ['summary', 'description', 'status', 'types', 'created_at', 'projects']
    readonly_fields = ['updated_at', 'created_at']


admin.site.register(Work, WorkAdmin),
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)


# Register your models here.
