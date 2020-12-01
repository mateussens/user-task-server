from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This name is already being used on another user.",
            )]
    )

    class Meta:
        model = User
        fields = '__all__'
