from django.contrib import admin
from authu import models


@admin.register(models.AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nickname',), }

