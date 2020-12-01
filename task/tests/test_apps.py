from django.apps import apps
from django.test import TestCase

from task.apps import TaskConfig


class TestAppConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(TaskConfig.name, 'task')
        self.assertEqual(apps.get_app_config('task').name, 'task')
