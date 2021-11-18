from django.contrib import admin
from .models import Category, Log

def make_status(modeladmin, request, queryset):
    queryset.update(status='assigned')
make_status.short_description = "Mark selected case as assigned"

class LogAdmin(admin.ModelAdmin):
    list_display = ['case', 'status']
    ordering = ['case']
    actions = [make_status]

admin.site.register(Category)
admin.site.register(Log, LogAdmin)
