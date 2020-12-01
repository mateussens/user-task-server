from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from user.models import User


class UserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_url = '/api/users/'
        self.user_1 = mommy.make(User, name="First User test")
        self.user_2 = mommy.make(User, name="Second User test")
        self.data = {
            "name": "User test"
        }

    def test_endpoint_create(self):
        response = self.client.post(
            self.user_url, self.data, format='json')
        assert response.status_code == 201

    def test_filters(self):
        response = self.client.get(
            self.user_url, format='json')
        assert response.json()['count'] == 2

    def test_filters_name(self):
        response = self.client.get(
            self.user_url + '?name=First', format='json')
        assert response.json()['count'] == 1
