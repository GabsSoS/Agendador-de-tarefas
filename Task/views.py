from rest_framework import generics
from Task.models import Task
from Task.serializers import TaskSerializer

# Create your views here.
class TaskCreateListAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer