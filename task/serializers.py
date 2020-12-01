from rest_framework import serializers

from task.models import Task
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = '__all__'
