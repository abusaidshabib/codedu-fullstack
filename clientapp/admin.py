from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'email')
