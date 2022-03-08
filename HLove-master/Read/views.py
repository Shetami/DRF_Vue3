from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .service import MangaFilters

from .serializers import MangaSerializer, MangaDetailSerializer, MangaReadSerializer

from .models import *


class MangaList(generics.ListAPIView):
    serializer_class = MangaSerializer
    filter_backends = (DjangoFilterBackend,)
    context_object_name = 'mangapost'
    filterset_class = MangaFilters
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        manga = Post.objects.all()
        return manga


class MangaDetailView(generics.RetrieveAPIView):

    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = MangaDetailSerializer


class MangaSliderView(generics.ListAPIView):
    serializer_class = MangaReadSerializer

    def get_queryset(self):
        return Page.objects.filter(manga__slug=self.kwargs['manga_slug'])


