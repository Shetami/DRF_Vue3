from rest_framework import serializers
from . import models


class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AuthUser
        fields = [
            'nickname',
            'planned',
            'read_list',
            'favorites_author',
            'favorites_tag',
        ]