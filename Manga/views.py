from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseRedirect
from authentication.models import Avatar
# Create your views here.
# from Manga.form import RegistrationForm
# from Manga.models.user import User


def home(request):
    avatar=get_object_or_404(Avatar,user=request.user)
    avatar_img=avatar.picture
    return render(request, 'home.html', {'avatar_img':avatar_img})


