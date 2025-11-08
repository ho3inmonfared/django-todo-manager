from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at', 'user')
    list_filter = ('completed', 'created_at', 'user')
    search_fields = ('title', 'description','user__username')
