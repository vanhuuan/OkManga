from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

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
        categories = request.POST.getlist("category")
        thumbnail = request.POST['thumbnailImg']
        description = request.POST['description']
        status = request.POST["status"]
        print("thumbnail:", thumbnail)
        new_manga = Manga.objects.create(author=author, name=name, thumbnail=thumbnail,
                                         status=status, description = description)
        for category in categories:
            new_manga.category.add(category)
        UserManga.objects.create(userId_id=userId, manga_id=new_manga.id)
        return home(request)
    else:
        listCategory = Category.objects.all()
        return render(request, 'add_manga.html', {"categories": listCategory})


@require_GET
def edit(request, manga_id):
    mg = Manga.objects.get(id=manga_id)
    listCategory = Category.objects.all()
    context = {"categories": listCategory, "manga": mg}
    return render(request, 'edit_manga.html', context)


@require_POST
def update(request):
    manga_id = request.POST['mangaId']
    name = request.POST['name']
    categories = request.POST.getlist("category")
    thumbnail = request.POST['thumbnailImg']
    description = request.POST['description']
    status = request.POST["status"]
    author = request.POST["author"]
    mg = Manga.get_manga_by_id(manga_id)
    mg.thumbnail = thumbnail
    mg.description = description
    mg.status = status
    mg.author = author
    mg.name = name
    mg.save()
    mg.category.clear()
    for category in categories:
        mg.category.add(category)

    return home(request)
