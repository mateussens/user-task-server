from django.test import TestCase
from model_mommy import mommy

from user.models import User
from user.serializers import UserSerializer


class UserTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(User, name="User test")

    def test_serializer_keys(self):
        serializer = UserSerializer(instance=self.user)

        expected = ['id', 'name', 'created_at', 'updated_at']
        assert set(serializer.data.keys()) == set(expected)
