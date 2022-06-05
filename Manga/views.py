from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from Manga.form import RegistrationForm
from Manga.models.user import User


def index(request):
    return render(request, "login.html")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = get_object_or_404(User, user_name=username)
        if user.password != password:
            return HttpResponse("User name or password is not correct")
        return render(request, "index.html", {'uid': user.id_user})
    except:
        return HttpResponse("User name or password is not correct")


def checkEmail(value):
    try:
        validate_email(value)
        return True
    except validate_email.ValidationError:
        return False


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})
