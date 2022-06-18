import email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm,ChangeAvatar
from .models import Avatar



# Create your views here.
def home(request):

    if request.user.is_authenticated:
        #avatar=get_object_or_404(Avatar, user=request.user)
        #avatar_img=avatar.picture
        # return render(request, 'home.html', {'avatar_img':avatar_img})
        return render(request, 'home.html')
    return render(request, 'home.html',{})


def login_user(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
       
        if user is not None:  # if user exist
            login(request, user)          
            messages.success(request, ('You are logged in'))
            request.session["user"] = user.id
            # avatar=get_object_or_404(Avatar,user=user)
            # avatar_img=avatar.picture
            # return render(request, 'home.html', {'avatar_img':avatar_img})
            return render(request, 'home.html')
           
            
        else:
            messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('authentication:login') 
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Youre now logged out'))
    return redirect('authentication:home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # avatar=Avatar(user=user,picture='authentication/avatar/person.jpg')
            # avatar.save()
            messages.success(request, 'You are now registered')
            return redirect('authentication:home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def edit_profile(request):
    avatar=get_object_or_404(Avatar,user=request.user)
    if request.method == 'POST':
        
        avatar_form=ChangeAvatar(request.POST,request.FILES,instance=avatar)
        form = EditProfileForm(request.POST, instance=request.user)

        if avatar_form.is_valid():
            form.save()
            # avatar_form.save()
            img=avatar_form.cleaned_data['picture']
            # avatar.picture=img
            # avatar.save()
            # messages.success(request, ('You have edited your profile'))               
            # avatar_img=avatar.picture
            # return render(request, 'home.html', {'avatar_img':avatar_img})
            return render(request, 'home.html')

    else:  # passes in user information
        form = EditProfileForm(instance=request.user)    
          
        avatar_form=ChangeAvatar(instance=avatar)    

    avatar_img=avatar.picture
    context = {'avatar_form':avatar_form,'form': form,'avatar_img':avatar_img}
    return render(request, 'edit_profile.html', context)


# return render(request, 'authenticate/edit_profile.html',{})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password'))
            # avatar=get_object_or_404(Avatar,user=request.user)
            # avatar_img=avatar.picture
            return render(request, 'home.html', {'avatar_img':avatar_img})
           
    else:  
        # passes in user information
        form = PasswordChangeForm(user=request.user)

        # avatar=get_object_or_404(Avatar,user=request.user)
        # avatar_img=avatar.picture
        context = {'form': form,'avatar_img':avatar_img}
        return render(request, 'change_password.html', context)
