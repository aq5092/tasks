from django.contrib import admin
from .models import Tasks
# from .models import Question
from .resources import TasksResource
from import_export.admin import ImportExportModelAdmin

@admin.register(Tasks)
class TaskAdmin(ImportExportModelAdmin):
    resource_classes = [TasksResource]
# admin.site.register(Tasks)
# Register your models here.
