from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Post, User
from django.shortcuts import render, get_object_or_404
from .forms import  EditProfileForm, PostForm, UserForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        # form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:  # if user exist
            login(request, user)
            # messages.success(request, ('Youre logged in'))
            return redirect('post_list')  # routes to 'home' on successful login
        else:
            # messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('login')
    else:
        return render(request, 'blog/login.html', {})


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id).last()
    return render(request, 'blog/profile.html', context={'user': user})


def logout_views(request):
    logout(request)
    return redirect("login")


@login_required    
def edit_profile(request):
    user = User.objects.filter(id=request.user.id).last()
    if request.method == "POST":
        form = EditProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successful." )
            return redirect('profile')
        else:
            messages.error(request, "Unsuccessful update. Invalid information.")
    else:
        form = EditProfileForm(instance=user)
    return render (request, "blog/edit_profile.html", {'form':form})


# @login_required
# def edit_profile(request):
#     print('mmmmmmmmmmmmmmmmmmmmmmmmmmmm')
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         # profile_form = UserForm(request.POST,  instance=request.User.profile)

#         if user_form.is_valid():
#             user_form.save()
#         # #     # profile_form.save()
#         # #     # messages.success(request, 'Your profile is updated successfully')
#             return redirect('profile')
#     else:
#         user_form = UserForm(instance=request.user)
#         # profile_form = UserForm(instance=request.user.profile)

#     return render(request, 'blog/edit_profile.html', {'user_form': user_form})

