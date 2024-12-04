from rest_framework import serializers
from otz.models import Tasks

class TaskSerializers(serializers.ModelSerializer):
    model = Tasks
    fields = '__all__'