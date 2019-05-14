from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.shortcuts import get_object_or_404
from api.models import Task, TaskList
from api.serializers import TaskListSerializer, TaskSerializer
from rest_framework import filters


class AllTaskLists(generics.ListCreateAPIView):
    # queryset = TaskList.objects.for_user(self.request.user)
    serializer_class = TaskListSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    # def get_serializer_class(self):
    #     return CategorySerializer2

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TLTasks (generics.ListCreateAPIView):
    serializer_class = TaskSerializer


    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        # try:
        #     category = TaskList.objects.get(id=self.kwargs.get('pk'))
        # except TaskList.DoesNotExist:
        #     raise Http404
        queryset = tasklist.tasks.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset
