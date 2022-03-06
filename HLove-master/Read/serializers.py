from rest_framework import serializers
from .models import *


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "image",
            "tags",
        )


class MangaDetailSerializer(serializers.ModelSerializer):
    manga_title = serializers.SlugRelatedField(slug_field="title", read_only=True)
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    language = serializers.SlugRelatedField(slug_field="language", read_only=True)
    tags = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)
    characters = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"


class MangaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            "page",
        )






