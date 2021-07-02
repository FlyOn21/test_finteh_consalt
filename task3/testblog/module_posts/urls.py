from django.urls import path
from . import views

urlpatterns = [
    path("",views.AllPosts.as_view(), name = "index"),
    path ("create/", views.CreatePostView.as_view(), name = "create"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("post_detail/<pk>",views.PostDetailView.as_view(), name="detail"),
    path("user_posts",views.UserPostsView.as_view(), name ="user_posts"),
]