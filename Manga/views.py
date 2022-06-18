from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseRedirect

from Manga.models.category import Category
from Manga.models.chapter import Chapter
from Manga.models.content import Content
from Manga.models.manga import Manga
from authentication.models import Avatar


# Create your views here.
# from Manga.form import RegistrationForm
# from Manga.models.user import User


def index(request):
    all_manga = Manga.objects.all()
    recent = all_manga.order_by("updated_at")[:12]
    hot = all_manga.order_by("views").reverse()[:12]
    categories = Category.objects.all().order_by("category")
    context = {'recent': recent, 'categories': categories, 'hot': hot}
    return render(request, 'index.html', context)


def home(request):
    avatar = get_object_or_404(Avatar, user=request.user)
    avatar_img = avatar.picture
    return render(request, 'home.html', {'avatar_img': avatar_img})


def all(request):
    all_manga = Manga.objects.all()
    categories = Category.objects.all().order_by("category")
    context = {'all_manga': all_manga, 'categories': categories}
    return render(request, 'all.html', context)


def recent(request):
    all_manga = Manga.objects.all().order_by("updated_at")
    categories = Category.objects.all().order_by("category")
    context = {'all_manga': all_manga, 'categories': categories}
    return render(request, 'recent.html', context)


def hot(request):
    all_manga = Manga.objects.all().order_by("views").reverse()
    categories = Category.objects.all().order_by("category")
    context = {'all_manga': all_manga, 'categories': categories}
    return render(request, 'hot.html', context)


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    all_manga = Manga.objects.filter(category=category)
    categories = Category.objects.all().order_by("category")
    context = {'all_manga': all_manga, 'categories': categories, 'category': category}
    return render(request, 'category.html', context)


def detail(request, manga_id):
    all_categories = Category.objects.all().order_by("category")
    manga = Manga.objects.get(id=manga_id)
    chapters = Chapter.objects.filter(manga=manga).order_by("index")
    categories = manga.category.all()
    context = {'manga': manga, 'categories': categories, 'chapters': chapters, 'all_categories': all_categories}
    return render(request, 'detail.html', context)


def view(request, chapter_id):
    categories = Category.objects.all().order_by("category")
    chapter = Chapter.objects.get(id=chapter_id)
    chapter_list = Chapter.objects.filter(manga=chapter.manga).order_by("index")
    content = Content.objects.filter(chapter=chapter).order_by("index")
    prev = None
    next = None
    try:
        prev = Chapter.objects.get(index=chapter.index + 1, manga=chapter.manga)
    except:
        pass
    try:
        next = Chapter.objects.get(index=chapter.index - 1, manga=chapter.manga)
    except:
        pass
    context = {'chapter': chapter, 'content': content, 'chapList': chapter_list, 'prevChap': prev, 'nextChap': next,
               'categories': categories}
    return render(request, 'view.html', context)
