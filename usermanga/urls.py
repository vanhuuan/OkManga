from django.urls import path, include

from usermanga import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('edit/<int:manga_id>/', views.edit, name="edit"),
    path('update', views.update, name="update"),
    path('addchapter/<int:manga_id>/', views.addChapter, name="addchapter"),
    path('create', views.create, name="create"),
    path('deletechap/<int:chapterId>', views.deleteChapter, name="deletechap"),
    path('deletemanga/<int:manga_id>', views.deleteManga, name="deletemanga"),
]