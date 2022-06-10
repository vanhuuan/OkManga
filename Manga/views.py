from django.shortcuts import render
from Manga.models.chapter import Chapter
from Manga.models.content import Content
from Manga.models.manga import Manga


def index(request):
    all_manga = Manga.objects.all()
    context = {'all_manga': all_manga}
    return render(request, 'index.html', context)

def detail(request, manga_id):
    manga = Manga.objects.get(id=manga_id)
    chapters = Chapter.objects.filter(manga=manga)
    categories = manga.category.all()
    context = {'manga': manga, 'categories': categories, 'chapters': chapters}
    return render(request, 'detail.html', context)

def view(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    content = Content.objects.filter(chapter=chapter)
    context = {'chapter': chapter, 'content': content, 'prevChap': chapter_id, 'nextChap': chapter_id}
    return render(request, 'view.html', context)