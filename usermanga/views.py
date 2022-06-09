from django.shortcuts import render, redirect

from Manga.models import manga
from Manga.models.category import Category
from Manga.models.manga import Manga
from usermanga.models import UserManga


def home(request):
    uid = request.user.id
    userManga = UserManga.get_all_user_manga(uid)
    return render(request, 'list_user_manga.html', {"mangas": userManga})


def add(request):
    if request.method == "POST":
        userId = request.user.id
        author = request.POST['author']
        name = request.POST['name']
        category = request.POST['category']
        thumbnail = request.POST['thumbnail']
        print(thumbnail)
        new_manga = Manga.objects.create(author=author, name=name, thumbnail=thumbnail,
                                         status="active")
        new_manga.category.add(category)
        UserManga.objects.create(userId_id=userId, manga_id=new_manga.id)
        return home(request)
    else:
        listCategory = Category.objects.all()
        return render(request, 'add_manga.html', {"categories": listCategory})
