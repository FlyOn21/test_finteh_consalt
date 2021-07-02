from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from .models import Posts, User, PostComments
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from module_posts.forms import LoginForm, RegistrationForm, CreatePostForm, CommentsForm, UpdatePostForm


class AllPosts(View):
    def get(self, request):
        queryset = Posts.objects.all()
        return render(request=request,
                      template_name="module_posts/index.html",
                      context={"posts": queryset})

    def post(self,request):
        Posts.objects.filter(id = request.POST.get("post_id")).delete()
        return redirect("/")


class PostDetailView(View):
    def get(self, request, pk):
        queryset_one = Posts.objects.get(id=pk)
        queryset_two = PostComments.objects.filter(post_id=pk)
        return render(request=request,
                      template_name="module_posts/post_detail.html",
                      context={"post": queryset_one, "comments": queryset_two})

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PostComments.objects.create(comment_text=data["comment_text"],
                                        post_id=data["post_id"])
        return redirect(reverse("detail", kwargs={"pk": request.POST.get("post_id")}), )

class UserPostsView(View):
    def get(self,request):
        queryset_one = User.objects.get(id = request.user.id)
        queryset_two= Posts.objects.filter(owner_user=queryset_one.email)
        return render(request=request,
                      template_name="module_posts/my_posts.html",
                      context={"posts": queryset_two})

class CreatePostView(View):
    def get(self, request):
        form = CreatePostForm()
        return render(
            request=request,
            template_name="module_posts/create_posts.html",
            context={"form": form}
        )

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if request.user.is_authenticated:
                print(request.user)
                user = User.objects.filter(email=request.user)[0]
                print(user)
                Posts.objects.create(
                    owner_user=user,
                    post_title=data["post_title"],
                    post_text=data["post_text"],
                    photo=data["photo"],
                )
            else:
                Posts.objects.create(
                    owner_user=data["owner_user"],
                    post_title=data["post_title"],
                    post_text=data["post_text"],
                    photo=data["photo"],
                )
        return redirect("/")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {"result": "init", "form": form}
        return render(
            request=request, template_name="module_posts/login.html", context=context
        )

    @csrf_exempt
    def post(self, request):
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            form = LoginForm()
            context = {"result": "Wrong", "form": form}
            return render(
                request=request, template_name="module_posts/login.html", context=context
            )
        return redirect("/")


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {"result": "init", "form": form}
        return render(
            request=request,
            template_name="module_posts/registration.html",
            context=context,
        )

    @csrf_exempt
    def post(self, request):
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            context = {"result": "Wrong", "form": form}
            return render(
                request=request,
                template_name="module_posts/registration.html",
                context=context,
            )
        form.save()
        return redirect("/login")
