from django_filters import rest_framework as filters

from task.models import Task


class TaskFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['user', 'description', 'is_open']
