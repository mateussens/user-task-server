import django_filters
from rest_framework import viewsets

from task.filter import TaskFilter
from task.models import Task
from task.serializers import TaskSerializer, TaskListSerializer
from userTask.common import ResultsSetPagination


class TaskViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing task instances.
    """
    serializer_class = TaskSerializer
    serializers = {
        'list': TaskListSerializer,
        'retrieve': TaskListSerializer
    }
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Task.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(TaskViewSet, self).filter_queryset(queryset)
        return queryset

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)
