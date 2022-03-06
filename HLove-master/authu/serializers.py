from rest_framework import serializers
from . import models


class UserAuthSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.AuthUser
        fields = "__all__"