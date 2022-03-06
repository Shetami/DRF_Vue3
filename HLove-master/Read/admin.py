from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


from .models import *


class PageInline(admin.TabularInline):
    model = Page
    readonly_fields = ('page_url',)


@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageInline]



admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(MangaTitle)
admin.site.register(MangaSeries)
admin.site.register(Language)
admin.site.register(Rating)
admin.site.register(Character)
