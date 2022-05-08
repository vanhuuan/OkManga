from django.contrib import admin

# Register your models here.
from Manga.models.chapter import Chapter
from Manga.models.comic import Comic
from Manga.models.content import Content
from Manga.models.genre import Genre
from Manga.models.history import History
from Manga.models.role import Role
from Manga.models.user import User

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Comic)
admin.site.register(Chapter)
admin.site.register(Content)
admin.site.register(History)
admin.site.register(Genre)
