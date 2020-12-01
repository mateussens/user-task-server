import django_filters
from rest_framework import viewsets

from user.filter import UserFilter
from user.models import User
from user.serializers import UserSerializer
from userTask.common import ResultsSetPagination


class UserViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing team instances.
    """
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilter
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return User.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(UserViewSet, self).filter_queryset(queryset)
        return queryset
