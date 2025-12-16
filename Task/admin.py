from django.contrib import admin
from Task.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'owner']