from rest_framework.response import Response
from rest_framework.decorators import api_view
from otz.models import Tasks
from .serializers import TaskSerializers

@api_view(['GET'])
def getData(request):
    task = Tasks.objects.all()
    serializer = TaskSerializers(task, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)