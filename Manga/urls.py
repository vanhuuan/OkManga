from django.urls import path

from . import views

app_name = 'Manga'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:manga_id>/', views.detail, name='detail'),
    path('view/<int:chapter_id>/', views.view, name='view'),
]
