from django.test import TestCase
from model_mommy import mommy

from task.models import Task
from task.serializers import TaskSerializer
from user.models import User


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(User, name="User test")
        self.task = mommy.make(Task, user_id=self.user.id, description="Task description", is_open=True)

    def test_serializer_keys(self):
        serializer = TaskSerializer(instance=self.task)

        expected = ['id', 'user', 'description', 'is_open', 'created_at', 'updated_at']
        assert set(serializer.data.keys()) == set(expected)
