from django.urls import path

from . import views

app_name = 'Manga'
urlpatterns = [
    path('', views.home, name='index'),
]
