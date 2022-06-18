from django.urls import path, include

from usermanga import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('edit/<int:manga_id>/', views.edit, name="edit"),
    path('update', views.update, name="update"),
]