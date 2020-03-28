from django.contrib import admin
from .models import Tech

class TechAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'position', 'email', 'phone')
    link_display_list = ('first_name', 'last_name')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'username', 'position', 'email', 'phone')


admin.site.register(Tech, TechAdmin)