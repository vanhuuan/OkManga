from django.urls import path, include

from usermanga import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
]