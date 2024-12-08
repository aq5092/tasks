from rest_framework import serializers
from otz.models import Tasks

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
    
    