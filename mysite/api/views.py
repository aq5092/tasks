from rest_framework.response import Response
from rest_framework.decorators import api_view
from otz.models import Tasks

from .serializers import TaskSerializers
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.permissions import IsAdminUser



class TaskDetail(APIView):
    def get(self, request):
        obj = Tasks.objects.all()
        ser = TaskSerializers(obj, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        ser = TaskSerializers(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)
    
    
class TaskInfo(APIView):
    def get(self, request, id):
        try:
            obj = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            msg = {'msg': 'not found'}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
        ser = TaskSerializers(obj)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            msg = {'msg': 'not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        ser = TaskSerializers(obj, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_205_RESET_CONTENT)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            msg = {'msg': 'not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        ser = TaskSerializers(obj, data = request.data, partial = True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_205_RESET_CONTENT)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            msg ={'msg': 'not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'msg': 'deleted'} , status=status.HTTP_204_NO_CONTENT)

""" 
class TaskList(viewsets.ModelViewSet):
    queryset =Tasks.objects.all()
    serializer_class = TaskSerializers

class TaskDetail(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers

class TaskUpdate(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers
 """
""" class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers
     """


""" class TaskAPIView(APIView):
    def get(self, request):
        listtask = Tasks.objects.all().values()
        return Response({'posts':list(listtask)})
    

    def detail(self, request):
        dettask = Tasks.objects.filter(pk=request.id)
        return Response({'detail': list(dettask)})

    def post(self, request):
        task_new = Tasks.objects.create(
            mavzu=request.data['mavzu'],
            nomer = request.data['nomer'],
            sana = request.data['sana'],
            muddat = request.data['muddat'],
            javobgar = request.data['javobgar'],
            topshiriq_turi = request.data['topshiriq_turi'],
            topshiriq_kimdan = request.data['topshiriq_kimdan'],
            status = request.data['status'],
            natijasi = request.data['natijasi']


        )
        return Response({'post': model_to_dict(task_new) })

 """
"""
class TaskAPIlist(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers

     Response({"id":"2","mavzu":"DjangoRF",
                         "nomer":"25XX777",
                        "sana":"2024-12-07T00:00:00Z",
                         "muddat":"2024-12-07T00:00:00Z","javobgar":"Qodirov A.",
                         "topshiriq_turi":"RP","topshiriq_kimdan":"QodirovA",
                         "status":"Jarayonda","natijasi":"Boshlanmadi"})
 

class TaskAPIView(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializers

 """

""" @api_view(['GET'])
def getData(request):
    task = Tasks.objects.all()
    serializer = TaskSerializers(task, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data) """