from django.shortcuts import render
from rest_framework import viewsets, generics, T
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
       tasks= Task.objects.filter(user=self.request.user)
       completed_param = self.request.GET.get('completed')
       search_param = self.request.GET.get("search")
       
       if  completed_param is not None:
           if completed_param.lower() == 'true':
               tasks = tasks.filter(completed= True)
           elif completed_param.lower() == 'false':
               tasks = tasks.filter(completed= False)    
               
       if search_param:
           tasks = tasks.filter(
               Q(title__icontains=search_param) |
               Q(description__icontains=search_param)
               ) 
       return tasks         

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    