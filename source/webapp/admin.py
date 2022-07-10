from django.contrib import admin

from webapp.models import Work, Type, Status


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['description']
    fields = ['description', 'status', 'created_at']
    # readonly_fields = ['status']


admin.site.register(Work, WorkAdmin),
admin.site.register(Type),
admin.site.register(Status),

# Register your models here.
