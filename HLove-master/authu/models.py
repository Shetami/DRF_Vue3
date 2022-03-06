from django.contrib.auth.models import User
from django.db import models

from Read.models import Post, Tag
from Read.service import upload, genirate_default_user_name


class AuthUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile1")
    nickname = models.CharField(max_length=50, unique=True, default=genirate_default_user_name)
    profile_image = models.ImageField(upload_to=upload, blank=True)
    slug = models.SlugField(max_length=50,  blank=True)
    planned = models.ManyToManyField(Post, blank=True, related_name='planned_list')
    ranked = models.BigIntegerField(null=True, blank=True, )
    read_list = models.ManyToManyField(Post, blank=True, related_name='readlist_list')
    favorites_author = models.ManyToManyField(Post, blank=True, related_name='favorites_author_list')
    favorites_tag = models.ManyToManyField(Tag, blank=True, related_name='favorites_tag_list')

    def __str__(self):
        return self.user.username


