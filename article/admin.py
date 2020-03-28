from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'vendor', 'type', 'expire_date', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('type', 'vendor')
    list_editable = ('is_published',)
    search_fields = ('title', 'vendor', 'type', 'expire_date', 'serial', 'tech')
    list_per_page = 25



admin.site.register(Article, ArticleAdmin)
