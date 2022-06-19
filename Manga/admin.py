from django.contrib import admin

# Register your models here.
from Manga.models.category import Category
from Manga.models.chapter import Chapter
from Manga.models.manga import Manga
from Manga.models.content import Content
from Manga.models.history import History


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['chapter__manga__name']
    ordering = ('chapter__manga__name', 'chapter__index', 'index')

class ChapterAdmin(admin.ModelAdmin):
    search_fields = ['manga__name']
    ordering = ('manga__name', 'index')

class MangaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('name',)

admin.site.register(Manga, MangaAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(History)
admin.site.register(Category)
