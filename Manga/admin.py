from django.contrib import admin

# Register your models here.
from Manga.models.category import Category
from Manga.models.chapter import Chapter
from Manga.models.manga import Manga
from Manga.models.content import Content
from Manga.models.history import History
from Manga.models.role import Role
from Manga.models.user import User

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Content)
admin.site.register(History)
admin.site.register(Category)
