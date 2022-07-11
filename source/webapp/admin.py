from django.contrib import admin

from webapp.models import Work, Type, Status


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['description', 'status', 'types']
    fields = ['summary', 'description', 'status', 'types', 'created_at']
    readonly_fields = ['updated_at', 'created_at']


admin.site.register(Work, WorkAdmin),
admin.site.register(Type)
admin.site.register(Status)

# Register your models here.
