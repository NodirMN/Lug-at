from django.contrib import admin
from .models  import Lugat


class LugatAdmin(admin.ModelAdmin):

    list_display = ['inglizcha', 'ozbekcha']

admin.site.register(Lugat, LugatAdmin)
# Register your models here.
