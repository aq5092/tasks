from django.db import models
from import_export import resources
from .models import Tasks

class TasksResource(resources.ModelResource):
    class Meta:
        model = Tasks
        
        skip_unchanged = True
        use_bulk = True