from django.contrib import admin
from .models import Area, CustomUser

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Area, AreaAdmin)
admin.site.register(CustomUser)