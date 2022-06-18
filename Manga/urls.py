from django.urls import path

from . import views

app_name = 'Manga'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:manga_id>/', views.detail, name='detail'),
    path('view/<int:chapter_id>/', views.view, name='view'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('recent/', views.recent, name='recent'),
    path('hot/', views.hot, name='hot'),
    path('all/', views.all, name='all')
]
