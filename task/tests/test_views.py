from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from task.models import Task
from user.models import User


class TaskTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.task_url = '/api/tasks/'
        self.user_1 = mommy.make(User, name="First User test")
        self.user_2 = mommy.make(User, name="Second User test")
        self.task_1 = mommy.make(Task, user_id=self.user_1.id, description="First task", is_open=True)
        self.task_2 = mommy.make(Task, user_id=self.user_2.id, description="Second task", is_open=False)
        self.data = {
            "user": self.user_1.id,
            "description": "Task description",
            "is_open": True
        }

    def test_endpoint_create(self):
        response = self.client.post(
            self.task_url, self.data, format='json')
        assert response.status_code == 201

    def test_filters(self):
        response = self.client.get(
            self.task_url, format='json')
        assert response.json()['count'] == 2

    def test_filters_is_open(self):
        response = self.client.get(
            self.task_url + '?is_open=false', format='json')
        assert response.json()['count'] == 1

    def test_filters_user(self):
        response = self.client.get(
            self.task_url + '?user={user}'.format(user=self.user_1.id), format='json')
        assert response.json()['count'] == 1

    def test_filters_description(self):
        response = self.client.get(
            self.task_url + '?description={description}'.format(description="First"), format='json')
        assert response.json()['count'] == 1
