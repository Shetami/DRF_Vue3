from django_filters import rest_framework as filters

from django.contrib.auth.models import User

from Read.models import Post


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilters(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__title', lookup_expr='in')
    author = CharFilterInFilter(field_name="author__name", lookup_expr='in')
    language = CharFilterInFilter(field_name="languages__language", lookup_expr='in')
    characters = CharFilterInFilter(field_name="characters__name", lookup_expr='in')

    class Meta:
        model = Post
        fields = ['tags', 'author', 'language', 'characters']


def upload(instance, filename):
    return "{0}/{1}".format(instance.manga.slug, filename)


def genirate_default_user_name():
    pk = User.objects.all().last().id
    return 'User_' + str(pk)
