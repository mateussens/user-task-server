from django_filters import rest_framework as filters

from user.models import User


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['name']
