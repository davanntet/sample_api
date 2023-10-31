from django.contrib import admin
from . import models
# Register your models here.
class Style (admin.ModelAdmin):
    list_display = ("id","firstname","lastname","age","sex")

admin.site.register(models.members,Style)

