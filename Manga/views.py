from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.http import HttpResponse

# Create your views here.
from Manga.models.user import User


def index(request):
    return render(request, "manga/templates/login.html")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = get_object_or_404(User, user_name=username)
        if user.password != password:
            return HttpResponse("account not correct")
        return HttpResponse("Login successfully")
    except:
        return HttpResponse("account not correct")


def checkEmail(value):
    try:
        validate_email(value)
        return True
    except validate_email.ValidationError:
        return False
