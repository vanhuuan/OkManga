from django.contrib import admin

# Register your models here.
from .models import Role,User,Comic,Chapter,Content,Comment

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Comic)
admin.site.register(Chapter)
admin.site.register(Content)
admin.site.register(Comment)